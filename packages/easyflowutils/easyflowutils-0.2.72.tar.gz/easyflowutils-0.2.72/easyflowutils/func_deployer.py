import os
import subprocess
import getpass


def deploy_func(func_name, region="europe-west9", source="."):
    try:
        subprocess.run("gcloud auth print-access-token", shell=True, check=True, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("You are not logged in to gcloud. Please provide your OAuth 2.0 token.")
        token = getpass.getpass("Enter your token: ")
        subprocess.run(f"gcloud auth activate-service-account --key-file={token}", shell=True, check=True)

    os.chdir(os.path.abspath(source))

    command = (
        f"gcloud functions deploy {func_name} "
        f"--gen2 "
        f"--runtime=python312 "
        f"--region={region} "
        f"--source={source} "
        f"--entry-point={func_name} "
        f"--trigger-http "
        f"--allow-unauthenticated"
    )
    subprocess.run(command, shell=True, check=True)


def get_current_project():
    result = subprocess.run(["gcloud", "config", "get-value", "project"],
                            capture_output=True, text=True, check=True)
    return result.stdout.strip()


def deploy_cloud_run(service_name, region="europe-west9", source=".", port=8080):
    try:
        subprocess.run("gcloud auth print-access-token", shell=True, check=True, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("You are not logged in to gcloud. Please provide your OAuth 2.0 token.")
        token = getpass.getpass("Enter your token: ")
        subprocess.run(f"gcloud auth activate-service-account --key-file={token}", shell=True, check=True)

    project_id = get_current_project()

    os.chdir(os.path.abspath(source))

    image_name = f"gcr.io/{project_id}/{service_name}:latest"
    build_command = f"gcloud builds submit --tag {image_name}"
    subprocess.run(build_command, shell=True, check=True)

    deploy_command = (
        f"gcloud run deploy {service_name} "
        f"--image {image_name} "
        f"--platform managed "
        f"--region {region} "
        f"--project {project_id} "
        f"--allow-unauthenticated "
        f"--port {port}"
    )

    subprocess.run(deploy_command, shell=True, check=True)
