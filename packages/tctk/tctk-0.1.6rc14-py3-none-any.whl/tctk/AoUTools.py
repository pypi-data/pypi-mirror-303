import os
import subprocess


class dsub:

    def __init__(
        self,
        docker_image: str,
        main_script_name: str,
        job_name: str,
        input_files_dict: {},
        output_files_dict: {},
        output_folder=None,
        log_file=None,
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
        self.main_script_name = main_script_name
        self.input_files_dict = input_files_dict
        self.output_files_dict = output_files_dict
        self.machine_type = machine_type
        self.disk_type = disk_type
        self.boot_disk_size = boot_disk_size
        self.disk_size = disk_size
        self.user_project = user_project
        self.project = project
        self.dsub_user_name = dsub_user_name
        self.user_name = user_name
        self.bucket = bucket
        self.job_name = job_name
        self.google_project = google_project
        self.region = region
        self.provider = provider
        self.preemptible = preemptible

        if output_folder is not None:
            self.output_folder = output_folder
        else:
            self.output_folder = (
                f"{self.bucket}/dsub/results/{{job-name}}/{{user-id}}/$(date +'%Y%m%d')/"
            )

        if log_file is not None:
            self.log_file = log_file
        else:
            self.log_file = (
                f"{self.bucket}/dsub/logs/{{job-name}}/{{user-id}}/$(date +'%Y%m%d')/"
                f"{{job-id}}-{{task-id}}-{{task-attempt}}.log"
            )

        print(
            "dsub initialized with parameters:\n",
            "main_script_name: " + self.main_script_name + "\n",
            "input_dict: " + str(self.input_files_dict) + "\n",
            "output_dict: " + str(self.output_folder) + "\n",
            "machine_type: " + self.machine_type + "\n",
            "disk_type: " + self.disk_type + "\n",
            "boot_disk_size: " + str(self.boot_disk_size) + "\n",
            "disk_size: " + str(self.disk_size) + "\n",
            "user_project: " + self.user_project + "\n",
            "project: " + self.project + "\n",
            "dsub_user_name: " + self.dsub_user_name + "\n",
            "user_name: " + self.user_name + "\n",
            "bucket: " + self.bucket + "\n",
            "job_name: " + self.job_name + "\n",
            "google_project: " + self.google_project + "\n"
        )

        self.script = ""

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
            f"--logging \"{self.log_file}\" \"$@\"" + " " +
            f"--name \"{self.job_name}\"" + " " +
            f"--env GOOGLE_PROJECT=\"{self.google_project}\"" + " "
        )

        input_flags = ""
        if len(self.input_files_dict) > 0:
            for k, v in self.input_files_dict.items():
                input_flags += f"--input {k}={v}" + " "

        output_flags = ""
        if len(self.output_folder) > 0:
            output_flags = ""
            for k, v in self.output_files_dict.items():
                output_flags += f"--env {k}=\"{v}\"" + " "
                output_flags += f"--output {k}_PATH={self.output_folder}{v}" + " "

        main_script = f"--script {self.main_script_name}"

        script = base_script + input_flags + output_flags + main_script
        if self.preemptible:
            script += " --preemptible"

        self.script = script

        return script

    def run(self, show_command=False):
        subprocess.run([self._dsub_script()], shell=True)
        if show_command:
            print()
            print("dsub command:")
            print(self.script.replace("--", "\\ \n--"))
