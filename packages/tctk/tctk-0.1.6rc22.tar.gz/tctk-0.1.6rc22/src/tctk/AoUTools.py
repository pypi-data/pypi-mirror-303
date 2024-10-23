import datetime
import os
import subprocess
import sys


class dsub:

    def __init__(
        self,
        docker_image: str,
        job_script_name: str,
        job_name: str,
        input_files_dict: {},
        multiple_output_files=False,
        output_file_name="",
        output_file_pattern="",
        output_folder=None,
        log_file_path=None,
        machine_type: str = "c3d-highcpu-4",
        disk_type="pd-ssd",
        boot_disk_size=50,
        disk_size=256,
        user_project=os.getenv("GOOGLE_PROJECT"),
        project=os.getenv("GOOGLE_PROJECT"),
        dsub_user_name=os.getenv("OWNER_EMAIL").split("@")[0],
        user_name=os.getenv("OWNER_EMAIL").split("@")[0].replace(".", "-"),
        bucket=os.getenv("WORKSPACE_BUCKET"),
        google_project=os.getenv("GOOGLE_PROJECT"),
        region="us-central1",
        provider="google-cls-v2",
        preemptible=False,
    ):
        self.docker_image = docker_image
        self.job_script_name = job_script_name
        self.input_files_dict = input_files_dict
        self.multiple_output_files = multiple_output_files
        self.output_file_name = output_file_name
        self.output_file_pattern = output_file_pattern
        self.machine_type = machine_type
        self.disk_type = disk_type
        self.boot_disk_size = boot_disk_size
        self.disk_size = disk_size
        self.user_project = user_project
        self.project = project
        self.dsub_user_name = dsub_user_name
        self.user_name = user_name
        self.bucket = bucket
        self.job_name = job_name.replace("_", "-")
        self.google_project = google_project
        self.region = region
        self.provider = provider
        self.preemptible = preemptible

        self.date = datetime.date.today().strftime("%Y%m%d")
        self.time = datetime.datetime.now().strftime("%H%M%S")

        if output_folder is not None:
            self.output_folder = output_folder
        else:
            self.output_folder = (
                f"{self.bucket}/dsub/results/{self.job_name}/{self.user_name}/{self.date}/{self.time}"
            )

        if log_file_path is not None:
            self.log_file_path = log_file_path
        else:
            self.log_file_path = (
                f"{self.bucket}/dsub/logs/{self.job_name}/{self.user_name}/{self.date}/{self.time}/{self.job_name}.log"
            )

        self.script = ""
        self.dsub_command = ""

        os.environ["PHEWAS_OUTPUT_FILE"] = (
            f"/mnt/data/output/{self.output_folder.replace(':/', '')}/{self.output_file_name}"
        )

    def _dsub_script(self):

        base_script = (
            f"dsub" + " " +
            f"--provider \"{self.provider}\"" + " " +
            f"--regions \"{self.region}\"" + " " +
            f"--machine-type \"{self.machine_type}\"" + " " +
            f"--disk-type \"{self.disk_type}\"" + " " +
            f"--boot-disk-size {self.boot_disk_size}" + " " +
            f"--disk-size {self.disk_size}" + " " +
            f"--user-project \"{self.user_project}\"" + " " +
            f"--project \"{self.project}\"" + " " +
            f"--image \"{self.docker_image}\"" + " " +
            f"--network \"network\"" + " " +
            f"--subnetwork \"subnetwork\"" + " " +
            f"--service-account \"$(gcloud config get-value account)\"" + " " +
            f"--user \"{self.dsub_user_name}\"" + " " +
            f"--logging {self.log_file_path} $@" + " " +
            f"--name \"{self.job_name}\"" + " " +
            f"--env GOOGLE_PROJECT=\"{self.google_project}\"" + " "
        )

        input_flags = ""
        if len(self.input_files_dict) > 0:
            for k, v in self.input_files_dict.items():
                input_flags += f"--input {k}={v}" + " "

        output_flag = ""
        if self.output_file_name != "":
            if self.multiple_output_files:
                if self.output_file_pattern != "":
                    output_flag += f"--output OUTPUT_FILES={self.output_folder}/{self.output_file_pattern}" + " "
                else:
                    print("Multiple output files require output_file_pattern.")
                    sys.exit(1)
            else:
                output_flag += f"--output OUTPUT_FILE={self.output_folder}/{self.output_file_name}" + " "
        else:
            print("output_file_name is required.")
            sys.exit(1)

        job_script = f"--script {self.job_script_name}"

        script = base_script + input_flags + output_flag + job_script

        if self.preemptible:
            script += " --preemptible"

        self.script = script

        return script

    def run(self, show_command=False):
        s = subprocess.run([self._dsub_script()], shell=True, capture_output=True, text=True)
        if s.returncode == 0:
            print(s.stdout)
            self.dsub_command = s.args[0].replace("--", "\\ \n--")
            if show_command:
                print()
                print("dsub command:")
                print(self.dsub_command)
        else:
            print(s.stderr)
