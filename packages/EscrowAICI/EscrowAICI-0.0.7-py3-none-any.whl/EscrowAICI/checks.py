import requests


def wkey_check(env, project, ao, token):
    get_wkey = requests.get(
        f"https://frontoffice.{env}.escrow.beekeeperai.com/wrapped-content-encryption-key/?project_id={project}",
        headers={
            "Content-type": "application/json",
            "Authorization": "Bearer " + token,
            "User-Agent": "curl/7.71.1",
        },
    )

    json = get_wkey.json()
    if len(json) == 0:
        return False
    for i in json:
        if i["is_ao_wcek"] == ao:
            return True

    return False


def algo_check(env, project, token):
    get_algo = requests.get(
        f"https://frontoffice.{env}.escrow.beekeeperai.com/algorithm/project/{project}/",
        headers={
            "Content-type": "application/json",
            "Authorization": "Bearer " + token,
        },
    )

    if len(get_algo.json()) == 0:
        return False
    else:
        return True, get_algo.json()[0]["id"]


def ds_check(env, project, token):
    get_ds = requests.get(
        f"https://frontoffice.{env}.escrow.beekeeperai.com/dataset/project/{project}",
        headers={
            "Content-type": "application/json",
            "Authorization": "Bearer " + token,
            "User-Agent": "curl/7.71.1",
        },
    )

    if len(get_ds.json()) == 0:
        return False
    else:
        return True, get_ds.json()[0]["id"]


def artifact_check(env, project, type, token):
    if type == "spec":
        name = "Data Specification"
    elif type == "attest":
        name = "Data Attestation"
    elif type == "valid":
        name = "Validation Criteria"
    else:
        return

    artifact_get = requests.get(
        f"https://frontoffice.{env}.escrow.beekeeperai.com/artifact/?project_id={project}",
        headers={
            "Content-type": "application/json",
            "Authorization": "Bearer " + token,
            "User-Agent": "curl/7.71.1",
        },
    )

    ajs = artifact_get.json()
    for i in ajs:
        if name in i["name"]:
            return True, i["id"]

    return False
