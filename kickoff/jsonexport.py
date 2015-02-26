from kickoff import app

from flask import jsonify

from kickoff.model import getReleases
from kickoff.firefoxdetails import primary_builds, beta_builds
from kickoff.firefoxversions import firefoxversions

from kickoff.thunderbirddetails import primary_builds as tb_primary_builds, beta_builds as tb_beta_builds
from kickoff.thunderbirdversions import thunderbirdversions

from kickoff.mobileversions import mobileversions
from kickoff.locales import languages


def getFilteredReleases(product, categories, lastRelease=None):
    version = []
    # we don't export esr in the version name
    if "major" in categories:
        version.append("([0-9]+\.[0-9]+|14\.0\.1)$")
    if "stability" in categories:
        version.append("([0-9]+\.[0-9]+\.[0-9]+|[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)")
    if "dev" in categories:
        version.append("[0-9]+\.[0-9](b|rc|build|plugin)[0-9]+$")
    if "esr" in categories:
        version.append("([0-9]+\.[0-9]+\.[0-9]+esr|[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+esr)")
    return [(r.version.replace("esr", ""), r._submittedAt.strftime("%Y-%m-%d")) for r in getReleases(ready=True, productFilter=product, versionFilterCategory=version, lastRelease=lastRelease)]


# Firefox JSON

@app.route('/json/firefox_history_major_releases.json', methods=['GET'])
def firefox_history_major_releases_json():
    # Match X.Y and 14.0.1 (special case)
    values = getFilteredReleases("firefox", "major")
    return jsonify(values)


@app.route('/json/firefox_history_stability_releases.json', methods=['GET'])
def firefox_history_stability_releases_json():
    # Match X.Y.Z (including esr) + W.X.Y.Z (example 1.5.0.8)
    values = getFilteredReleases("firefox", "stability")
    return jsonify(values)


@app.route('/json/firefox_history_development_releases.json', methods=['GET'])
def firefox_history_development_releases_json():
    # Match 23.b2, 1.0rc2, 3.6.3plugin1 or 3.6.4build7
    values = getFilteredReleases("firefox", "dev")
    return jsonify(values)


@app.route('/json/firefox_versions.json', methods=['GET'])
def firefox_versions_json():
    # Stable
    lastStable = getFilteredReleases("firefox", ["major", "stability"], lastRelease=True)
    firefoxversions["LATEST_FIREFOX_VERSION"] = lastStable[0][0]
    # beta
    lastStable = getFilteredReleases("firefox", ["dev"], lastRelease=True)
    firefoxversions["LATEST_FIREFOX_DEVEL_VERSION"] = lastStable[0][0]
    firefoxversions["LATEST_FIREFOX_RELEASED_DEVEL_VERSION"] = lastStable[0][0]
    # esr
    lastStable = getFilteredReleases("firefox", ["esr"], lastRelease=True)
    firefoxversions["FIREFOX_ESR"] = lastStable[0][0]+"esr"
    return jsonify(firefoxversions)


def replaceValue(array, versionTag, version):
    for locale, datalist in array.iteritems():
        i = 0
        for ver in datalist:
            if ver == versionTag:
                array[locale][i] = version
            i += 1


def updateBuilds(product, primary_builds):
    # Stable
    lastStable = getFilteredReleases(product, ["major", "stability"], lastRelease=True)
    replaceValue(primary_builds, "LATEST_FIREFOX_VERSION", lastStable[0][0])

    # beta
    lastStable = getFilteredReleases(product, ["dev"], lastRelease=True)
    replaceValue(primary_builds, "LATEST_FIREFOX_DEVEL_VERSION", lastStable[0][0])
    replaceValue(primary_builds, "LATEST_FIREFOX_RELEASED_DEVEL_VERSION", lastStable[0][0])

    # esr
    lastStable = getFilteredReleases(product, ["esr"], lastRelease=True)
    replaceValue(primary_builds, "FIREFOX_ESR", lastStable[0][0]+"esr")
    replaceValue(primary_builds, "LATEST_FIREFOX_OLDER_VERSION", firefoxversions['LATEST_FIREFOX_OLDER_VERSION'])
    replaceValue(primary_builds, "FIREFOX_AURORA", "38")
#    return primary_builds


@app.route('/json/firefox_primary_builds.json', methods=['GET'])
def firefox_primary_builds_json():
    updateBuilds("firefox", primary_builds)
    return jsonify(primary_builds)


@app.route('/json/firefox_beta_builds.json', methods=['GET'])
def firefox_beta_builds_json():
    updateBuilds("firefox", beta_builds)
    return jsonify(beta_builds)


# Mobile JSON


@app.route('/json/mobile_details.json', methods=['GET'])
def mobile_details_json():
    lastStable = getFilteredReleases("fennec", ["major", "stability"], lastRelease=True)
    mobileversions['version'] = lastStable[0][0]
    lastBeta = getFilteredReleases("fennec", ["beta"], lastRelease=True)
    mobileversions['beta_version'] = lastBeta[0][0]
    return jsonify(mobileversions)


@app.route('/json/mobile_history_major_releases.json', methods=['GET'])
def mobile_history_major_releases_json():
    values = getFilteredReleases("fennec", "major")
    return jsonify(values)


@app.route('/json/mobile_history_stability_releases.json', methods=['GET'])
def mobile_history_history_releases_json():
    values = getFilteredReleases("fennec", "stability")
    return jsonify(values)


@app.route('/json/mobile_history_development_releases.json', methods=['GET'])
def mobile_history_development_releases_json():
    # Match 23.b2, 1.0rc2, 3.6.3plugin1 or 3.6.4build7
    values = getFilteredReleases("fennec", "dev")
    return jsonify(values)

# THUNDERBIRD JSON


@app.route('/json/thunderbird_history_major_releases.json', methods=['GET'])
def thunderbird_history_major_releases_json():
    values = getFilteredReleases("thunderbird", "major")
    return jsonify(values)


@app.route('/json/thunderbird_history_stability_releases.json', methods=['GET'])
def thunderbird_history_history_releases_json():
    values = getFilteredReleases("thunderbird", "stability")
    return jsonify(values)


@app.route('/json/thunderbird_history_development_releases.json', methods=['GET'])
def thunderbird_history_development_releases_json():
    # Match 23.b2, 1.0rc2, 3.6.3plugin1 or 3.6.4build7
    values = getFilteredReleases("thunderbird", "dev")
    return jsonify(values)


@app.route('/json/thunderbird_versions.json', methods=['GET'])
def thunderbird_versions_json():
    # Stable
    lastStable = getFilteredReleases("thunderbird", ["major", "stability"], lastRelease=True)
    thunderbirdversions["LATEST_THUNDERBIRD_VERSION"] = lastStable[0][0]
    return jsonify(thunderbirdversions)


@app.route('/json/thunderbird_primary_builds.json', methods=['GET'])
def thunderbird_primary_builds_json():
    # default values
    lastStable = getFilteredReleases("thunderbird", ["major", "stability"], lastRelease=True)
    common = {lastStable[0][0]: {'Windows': {'filesize': 25.1}, 'OS X': {'filesize': 50.8}, 'Linux': {'filesize': 31.8}}}
    tb_prim = {}
    for key in tb_primary_builds:
        tb_prim[key] = common
    return jsonify(tb_prim)


@app.route('/json/thunderbird_beta_builds.json', methods=['GET'])
def thunderbird_beta_builds_json():
    return jsonify(tb_beta_builds)


# COMMON JSON

@app.route('/json/languages.json', methods=['GET'])
def languages_json():
    return jsonify(languages)
