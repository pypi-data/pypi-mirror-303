import os
import sys
from ramalama.common import exec_cmd, default_image, in_container, genname
from ramalama.version import version


file_not_found = """\
RamaLama requires the "%s" command to be installed on the host when running with --nocontainer.
RamaLama is designed to run AI Models inside of containers, where "%s" is already installed.
Either install a package containing the "%s" command or run the workload inside of a container.
"""

file_not_found_in_container = """\
RamaLama requires the "%s" command to be installed inside of the container.
RamaLama requires the server application be installed in the container images.
Either install a package containing the "%s" command in the container or run
with the default RamaLama image.
"""


class Model:
    """Model super class"""

    model = ""
    type = "Model"
    common_params = ["-c", "2048"]

    def __init__(self, model):
        self.model = model
        if sys.platform == "darwin" or os.getenv("HIP_VISIBLE_DEVICES") or os.getenv("CUDA_VISIBLE_DEVICES"):
            self.common_params += ["-ngl", "99"]

    def login(self, args):
        raise NotImplementedError(f"ramalama login for {self.type} not implemented")

    def logout(self, args):
        raise NotImplementedError(f"ramalama logout for {self.type} not implemented")

    def path(self, source, args):
        raise NotImplementedError(f"ramalama path for {self.type} not implemented")

    def pull(self, args):
        raise NotImplementedError(f"ramalama pull for {self.type} not implemented")

    def push(self, source, args):
        raise NotImplementedError(f"ramalama push for {self.type} not implemented")

    def is_symlink_to(self, file_path, target_path):
        if os.path.islink(file_path):
            symlink_target = os.readlink(file_path)
            abs_symlink_target = os.path.abspath(os.path.join(os.path.dirname(file_path), symlink_target))
            abs_target_path = os.path.abspath(target_path)
            return abs_symlink_target == abs_target_path

        return False

    def garbage_collection(self, args):
        repo_paths = ["huggingface", "oci", "ollama"]
        for repo in repo_paths:
            repo_dir = f"{args.store}/repos/{repo}"
            model_dir = f"{args.store}/models/{repo}"
            for root, dirs, files in os.walk(repo_dir):
                file_has_a_symlink = False
                for file in files:
                    file_path = os.path.join(root, file)
                    if (repo == "ollama" and file.startswith("sha256:")) or file.endswith(".gguf"):
                        file_path = os.path.join(root, file)
                        for model_root, model_dirs, model_files in os.walk(model_dir):
                            for model_file in model_files:
                                if self.is_symlink_to(os.path.join(root, model_root, model_file), file_path):
                                    file_has_a_symlink = True

                        if not file_has_a_symlink:
                            os.remove(file_path)
                            file_path = os.path.basename(file_path)
                            print(f"Deleted: {file_path}")

    def remove(self, args):
        symlink_path = self.symlink_path(args)
        if os.path.exists(symlink_path):
            try:
                os.remove(symlink_path)
                print(f"Untagged: {self.model}")
            except OSError as e:
                if not args.ignore:
                    raise KeyError(f"removing {self.model}: {e}")
        else:
            if not args.ignore:
                raise KeyError(f"model {self.model} not found")

        self.garbage_collection(args)

    def symlink_path(self, args):
        raise NotImplementedError(f"symlink_path for {self.type} not implemented")

    def run(self, args):
        prompt = "You are a helpful assistant"
        if args.ARGS:
            prompt = " ".join(args.ARGS)

        # Build a prompt with the stdin text that prepend the prompt passed as an
        # argument to ramalama cli
        if not sys.stdin.isatty():
            input = sys.stdin.read()
            prompt = input + "\n\n" + prompt

        symlink_path = self.pull(args)
        exec_args = [
            "llama-cli",
            "-m",
            symlink_path,
            "--in-prefix",
            "",
            "--in-suffix",
            "",
            "--no-display-prompt",
            "-p",
            prompt,
        ] + self.common_params
        if not args.ARGS and sys.stdin.isatty():
            exec_args.append("-cnv")

        try:
            exec_cmd(exec_args, False)
        except FileNotFoundError as e:
            if in_container():
                raise NotImplementedError(file_not_found_in_container % (exec_args[0], str(e).strip("'")))
            raise NotImplementedError(file_not_found % (exec_args[0], exec_args[0], exec_args[0], str(e).strip("'")))

    def serve(self, args):
        symlink_path = self.pull(args)
        exec_args = ["llama-server", "--port", args.port, "-m", "/run/model"]
        if args.runtime == "vllm":
            exec_args = ["vllm", "serve", "--port", args.port, "/run/model"]

        if args.generate == "quadlet":
            return self.quadlet(symlink_path, args, exec_args)

        if args.generate == "kube":
            return self.kube(symlink_path, args, exec_args)

        try:
            exec_cmd(exec_args)
        except FileNotFoundError as e:
            if in_container():
                raise NotImplementedError(file_not_found_in_container % (exec_args[0], str(e).strip("'")))
            raise NotImplementedError(file_not_found % (exec_args[0], exec_args[0], exec_args[0], str(e).strip("'")))

    def quadlet(self, model, args, exec_args):
        port_string = ""
        if hasattr(args, "port"):
            port_string = f"PublishPort={args.port}"

        name_string = ""
        if hasattr(args, "name") and args.name:
            name_string = f"ContainerName={args.name}"

        print(
            f"""
[Unit]
Description=RamaLama {args.UNRESOLVED_MODEL} AI Model Service
After=local-fs.target

[Container]
AddDevice=-/dev/dri
AddDevice=-/dev/kfd
Exec={" ".join(exec_args)}
Image={default_image()}
Volume={model}:/run/model:ro,z
{name_string}
{port_string}

[Install]
# Start by default on boot
WantedBy=multi-user.target default.target
"""
        )

    def _gen_ports(self, args):
        if not hasattr(args, "port"):
            return ""

        p = args.port.split(":", 2)
        ports = f"""\
    ports:
    - containerPort: {p[0]}"""
        if len(p) > 1:
            ports += f"""
      hostPort: {p[1]}"""

        return ports

    def _gen_volumes(self, model, args):
        mounts = """\
    volumeMounts:
    - mountPath: /run/model
      name: model"""

        volumes = f"""
  volumes:
  - name model
    hostPath:
      path: {model}"""

        for dev in ["dri", "kfd"]:
            if os.path.exists("/dev/" + dev):
                mounts = (
                    mounts
                    + f"""
    - mountPath: /dev/{dev}
      name: {dev}"""
                )
                volumes = (
                    volumes
                    + f""""
  - name {dev}
    hostPath:
      path: /dev/{dev}"""
                )

        return mounts + volumes

    def kube(self, model, args, exec_args):
        port_string = self._gen_ports(args)
        volume_string = self._gen_volumes(model, args)
        _version = version()
        if hasattr(args, "name") and args.name:
            name = args.name
        else:
            name = genname()

        print(
            f"""\
# Save the output of this file and use kubectl create -f to import
# it into Kubernetes.
#
# Created with ramalama-{_version}
apiVersion: v1
kind: Deployment
metadata:
  labels:
    app: {name}
  name: {name}
spec:
  containers:
  - name: {name}
    image: {args.image}
    command: ["{exec_args[0]}"]
    args: {exec_args[1:]}
{port_string}
{volume_string}"""
        )
