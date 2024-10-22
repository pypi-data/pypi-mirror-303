import requests
from EscrowAICI import general
import sseclient
import os
import json
from azure.storage.blob import BlobClient


def upload_algo(
    env, project, org, name, description, compute, memory, machine, type, file, token
):
    artifacts = find_artifacts(env, project, type, token)
    attest = artifacts[0]
    valid = artifacts[1]
    wkey = find_wkey(env, project, token)

    if compute == "Intel SGX":
        response = requests.post(
            f"https://frontoffice.{env}.escrow.beekeeperai.com/composite/algorithm/",
            headers={"Authorization": "Bearer " + token},
            data={
                "algorithm": '"{\\"name\\":\\"'
                + name
                + '\\",\\"description\\":\\"'
                + ""
                + '\\",\\"project\\":\\"'
                + project
                + '\\",\\"organization\\":\\"'
                + org
                + '\\"}"',
                "version_tag": "v1",
                "description": description,
                "algorithm_type": type,
                "validation_criteria_version": valid,
                "data_attestation_version": attest,
                "has_phi_agreement": "true",
                "upload_file_name": os.path.basename(file),
                "upload_type": "Upload Zip",
                "wcek_version": wkey,
                "sgx_memory": memory,
                "machine_type": machine,
                "is_fortanix_sgx_enabled": "true",
                "is_microsoft_aci_enabled": "false",
                "is_cvm_enabled": "false",
            },
            files=[("0", (file, open(file, "rb"), "application/zip"))],
        )
    if compute == "Microsoft ACI":
        response = requests.post(
            f"https://frontoffice.{env}.escrow.beekeeperai.com/composite/algorithm/",
            headers={"Authorization": "Bearer " + token},
            data={
                "algorithm": '"{\\"name\\":\\"'
                + name
                + '\\",\\"description\\":\\"'
                + ""
                + '\\",\\"project\\":\\"'
                + project
                + '\\",\\"organization\\":\\"'
                + org
                + '\\"}"',
                "version_tag": "v1",
                "description": description,
                "algorithm_type": type,
                "validation_criteria_version": valid,
                "data_attestation_version": attest,
                "has_phi_agreement": "true",
                "upload_file_name": os.path.basename(file),
                "upload_type": "Upload Zip",
                "wcek_version": wkey,
                "is_fortanix_sgx_enabled": "false",
                "is_microsoft_aci_enabled": "true",
                "is_cvm_enabled": "false",
            },
            files=[("0", (file, open(file, "rb"), "application/zip"))],
        )
    if compute == "CVM":
        response = requests.post(
            f"https://frontoffice.{env}.escrow.beekeeperai.com/composite/algorithm/",
            headers={"Authorization": "Bearer " + token},
            data={
                "algorithm": '"{\\"name\\":\\"'
                + name
                + '\\",\\"description\\":\\"'
                + ""
                + '\\",\\"project\\":\\"'
                + project
                + '\\",\\"organization\\":\\"'
                + org
                + '\\"}"',
                "version_tag": "v1",
                "description": description,
                "algorithm_type": type,
                "validation_criteria_version": valid,
                "data_attestation_version": attest,
                "has_phi_agreement": "true",
                "upload_type": "Upload Zip",
                "upload_file_name": os.path.basename(file),
                "wcek_version": wkey,
                "is_fortanix_sgx_enabled": "false",
                "is_microsoft_aci_enabled": "false",
                "is_cvm_enabled": "true",
            },
            files=[("0", (file, open(file, "rb"), "application/zip"))],
        )

    return response


def upload_algo_version(
    env, project, algo_id, version, description, compute, type, file, token
):
    sgx = False
    aci = False
    cvm = False
    if compute == "Intel SGX":
        sgx = True
    if compute == "Microsoft ACI":
        aci = True
    if compute == "CVM":
        cvm = True

    artifacts = find_artifacts(env, project, type, token)
    attest = artifacts[0]
    valid = artifacts[1]
    wkey = find_wkey(env, project, token)

    algo_get = requests.get(
        f"https://frontoffice.{env}.escrow.beekeeperai.com/algorithm/{algo_id}/",
        headers={
            "Content-type": "application/json",
            "Authorization": "Bearer " + token,
            "User-Agent": "curl/7.71.1",
        },
    )
    if algo_get.status_code != 200:
        return algo_get

    try:
        response = requests.post(
            f"https://frontoffice.{env}.escrow.beekeeperai.com/algorithm-version/",
            headers={
                "Authorization": "Bearer " + token,
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
            },
            data={
                "algorithm": algo_id,
                "version_tag": version,
                "description": description,
                "algorithm_type": type,
                "validation_criteria_version": valid,
                "data_attestation_version": attest,
                "upload_type": "Upload Zip",
                "upload_file_name": os.path.basename(file),
                "has_phi_agreement": "true",
                "wcek_version": wkey,
                "is_fortanix_sgx_enabled": str(sgx),
                "is_microsoft_aci_enabled": str(aci),
                "is_cvm_enabled": str(cvm),
            },
            files=[("0", (file, open(file, "rb"), "application/zip"))],
        )

        return response
    except Exception as e:
        print("Error uploading algo version to Escrow")
        print(e)
        raise (e)


def finish_algo_upload(env, file, response, algo_id, compute, token):
    sgx = False
    aci = False
    cvm = False
    if compute == "Intel SGX":
        sgx = True
    if compute == "Microsoft ACI":
        aci = True
    if compute == "CVM":
        cvm = True
    data = response.json()

    version_id = data["algorithm_version_id"]
    url = data["upload_url"]
    client = BlobClient.from_blob_url(url)

    with open(file, "rb") as upload:
        client.upload_blob(upload, overwrite=True)

    patch = requests.patch(
        f"https://frontoffice.{env}.escrow.beekeeperai.com/algorithm-version/{version_id}/",
        headers={"Authorization": "Bearer " + token, "User-Agent": "curl/7.71.1"},
        data={
            "status": "In Progress",
            "algorithm": algo_id,
            "is_fortanix_sgx_enabled": str(sgx),
            "is_microsoft_aci_enabled": str(aci),
            "is_cvm_enabled": str(cvm),
        },
        files=[("0", (file, open(file, "rb"), "application/zip"))],
    )

    return patch


def get_algo_notification(env, project, compute, token):
    client = sseclient.SSEClient(
        f"https://notification.{env}.escrow.beekeeperai.com/project-notifications/{project}/?token={token}"
    )
    docker = False
    if compute == "Intel SGX":
        enclave = False
    else:
        enclave = True
    for event in client:
        if event.event != "stream-open" and event.event != "keep-alive":
            if event.data != "":
                message = json.loads(event.data)["message"]
                print(f"\033[1m\033[92mESCROWAI: \033[0m\033[0m{message}")
                if message == "Docker Push Succeeded":
                    docker = True
                if message == "EnclaveOS Build Succeded":
                    enclave = True
                if docker and enclave:
                    return True
                if (
                    message == "File Validation Failed"
                    or message == "EnclaveOS Build Failed"
                ):
                    return False


def upload_run_config(
    env,
    project,
    name,
    description,
    algo_version,
    ds_version,
    compute,
    memory,
    type,
    token,
):
    versions = general.find_algo_ds_versions(
        env, project, algo_version, ds_version, token
    )

    response = requests.post(
        f"https://frontoffice.{env}.escrow.beekeeperai.com/run-configuration/",
        headers={"Authorization": "Bearer " + token, "User-Agent": "curl/7.71.1"},
        data={
            "algorithm_version": versions[0],
            "dataset_version": versions[1],
            "project": project,
            "name": name,
            "description": description,
            "test_type": "Regular",
            "run_type": type,
            "confidential_compute_technology": compute,
            "algo_container_memory": memory,
        },
    )

    return response


def send_notification(
    env,
    project,
    algo_version,
    ds_version,
    memory,
    machines,
    machine,
    training_parameters,
    token,
):
    rc = general.find_run_config(env, project, algo_version, ds_version, token)

    if machine == "":
        response = requests.post(
            f"https://frontoffice.{env}.escrow.beekeeperai.com/algorithm-version/{rc}/run/",
            headers={"Authorization": "Bearer " + token, "User-Agent": "curl/7.71.1"},
            data={
                "run_timeout": 30,
                "algo_container_cpus": machines,
                "algo_container_memory": memory,
                "run_configuration": rc,
                "training_parameters": training_parameters,
            },
        )
    else:
        response = requests.post(
            f"https://frontoffice.{env}.escrow.beekeeperai.com/algorithm-version/{rc}/run/",
            headers={"Authorization": "Bearer " + token, "User-Agent": "curl/7.71.1"},
            data={
                "run_timeout": 30,
                "run_configuration": rc,
                "machine_type": machine,
                "training_parameters": training_parameters,
            },
        )

    return response


def download_report(env, project, token):
    configs = requests.get(
        f"https://frontoffice.{env}.escrow.beekeeperai.com/run-configuration/?project_id={project}",
        headers={"Authorization": "Bearer " + token, "User-Agent": "curl/7.71.1"},
    )

    if configs.status_code != 200:
        print("\033[1m\033[36mCLIENT:\033[0m\033[0m ERROR: ", configs.status_code)
        print(configs.text)
        return False

    config_id = configs.json()[0]["id"]

    report_response = requests.get(
        f"https://frontoffice.{env}.escrow.beekeeperai.com/report/?run_configuration={config_id}",
        headers={"User-Agent": "curl/7.71.1", "Authorization": "Bearer " + token},
    )

    if report_response.status_code == 200:
        output = report_response.json()[0]["json_data"][12:-2]
        f = open("downloads/report.txt", "w")
        f.write(output)
        f.close()

    return report_response


def find_artifacts(env, project, type, token):
    artifact_get = requests.get(
        f"https://frontoffice.{env}.escrow.beekeeperai.com/artifact/?project_id={project}",
        headers={
            "Content-type": "application/json",
            "Authorization": "Bearer " + token,
            "User-Agent": "curl/7.71.1",
        },
    )

    ajs = artifact_get.json()

    attest = ""
    valid = ""
    for i in ajs:
        if "Attestation" in i["name"]:
            attest = i["id"]
        if "Validation" in i["name"]:
            valid = i["id"]

    artifact_v_get = requests.get(
        f"https://frontoffice.{env}.escrow.beekeeperai.com/artifact-version/?artifact_id={attest}",
        headers={
            "Content-type": "application/json",
            "Authorization": "Bearer " + token,
            "User-Agent": "curl/7.71.1",
        },
    )
    attest_id = artifact_v_get.json()[0]["id"]

    valid_id = None
    if type == "validation":
        artifact_v_get = requests.get(
            f"https://frontoffice.{env}.escrow.beekeeperai.com/artifact-version/?artifact_id={valid}",
            headers={
                "Content-type": "application/json",
                "Authorization": "Bearer " + token,
                "User-Agent": "curl/7.71.1",
            },
        )
        valid_id = artifact_v_get.json()[0]["id"]

    return attest_id, valid_id


def find_wkey(env, project, token):
    return general.find_keys(env, project, True, token)[2]
