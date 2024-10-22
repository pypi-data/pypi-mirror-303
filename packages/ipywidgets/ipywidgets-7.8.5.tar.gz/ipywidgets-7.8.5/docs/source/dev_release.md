Developer Release Procedure
===========================

To release a new version of the widgets on PyPI and npm, first checkout master
and cd into the repo root.

```
cd release
conda deactivate
conda remove --all -y -n releasewidgets
rm -rf ipywidgets

conda create -c conda-forge --override-channels -y -n releasewidgets "nodejs==16.*" "yarn=3" twine jupyterlab=4 jupyter-packaging jq python==3.9
conda activate releasewidgets

git clone git@github.com:jupyter-widgets/ipywidgets.git
cd ipywidgets
```


### Fix the widget spec

If there were changes in the widget model specification (i.e., any change made
to any widget attributes), we need to update the model specification version and
record the documented attributes.

First, update the relevant model specification versions. For example, the commit https://github.com/jupyter-widgets/ipywidgets/commit/fca6f355605dc9e04062ce0eec4a7acbb5632ae2 updated the controls model version. We follow the semver spec for model version numbers, so model changes that are backwards-incompatible should be major version bumps, while backwards-compatible additions should be minor version bumps.

Next, regenerate the model spec with the new version numbers by doing something like this in the repository root directory:
```
(pip install -e .)
python ./packages/schema/generate-spec.py > packages/schema/jupyterwidgetmodels.latest.md
```

Copy `packages/schema/jupyterwidgetmodels.latest.md` to an appropriately-named
markdown file (see the existing model spec files in that directory for the
naming convention). This documents the widget model specification for a specific ipywidget
release.

Commit the changes (don't forget to `git add` the new model spec file).

### Publish the npm modules

```
# clean out all dirty files
git checkout 7.x
git pull origin 7.x
git reset --hard origin/7.x
git clean -fdx
jlpm install
yarn publish
```

Lerna will prompt you for version numbers for each of the changed npm packages. Lerna will then change the versions appropriately (including the interdependency versions), commit, tag, and publish the new packages to npm.

### Fix NPM tags!!!

NPM is stupid, it can't see you just published versions that are prior to the latest (You are on the 7.x branch, so not publishing the latest of ipywidgets packages). It will mark your packages as "latest", this will have the impact of breaking users flow because e.g. they will now pull an outdated html-manager in nbconvert.

You need to fix the tags for all the packages you just publish with e.g. (PLEASE VERIFY VERSION NUMBERS, CHECKING THE ACTUAL LATEST):

```
npm dist-tag add @jupyter-widgets/jupyterlab-manager@5.0.13 latest
npm dist-tag add @jupyter-widgets/base@6.0.10 latest
npm dist-tag add @jupyter-widgets/controls@5.0.11 latest
npm dist-tag add @jupyter-widgets/html-manager@1.0.13 latest
npm dist-tag add @jupyter-widgets/output@6.0.10 latest
```

### jupyterlab_widgets

Go into the `jupyterlab_widgets` directory. Change `jupyterlab_widgets/_version.py` to reflect the new version number.
```
(cd jupyterlab_widgets && python setup.py sdist bdist_wheel &&  twine check dist/* && twine upload dist/*)
```

Verify that the package is uploaded.
```
curl -s https://pypi.org/pypi/jupyterlab-widgets/json | jq  -r '[.releases[][] | [.upload_time, .digests.sha256, .filename] | join(" ")] | sort '
```

### widgetsnbextension

Go into the `widgetsnbextension` directory. Change `widgetsnbextension/_version.py` to reflect the new version number.
```
(cd widgetsnbextension && python setup.py sdist && python setup.py bdist_wheel --universal && twine upload dist/*)
```

Verify that the package is uploaded.
```
curl -s https://pypi.org/pypi/widgetsnbextension/json | jq  -r '[.releases[][] | [.upload_time, .digests.sha256, .filename] | join(" ")] | sort '
```

### ipywidgets

Change `ipywidgets/_version.py` to reflect the new version number, and if necessary, a new `__html_manager_version__`. Change the `install_requires` parameter in `setup.py` reference the new widgetsnbextension version.

```
(python setup.py sdist && python setup.py bdist_wheel --universal && twine upload dist/*)
```

Verify that the package is uploaded:
```
curl -s https://pypi.org/pypi/ipywidgets/json | jq  -r '[.releases[][] | [.upload_time, .digests.sha256, .filename] | join(" ")] | sort '
```

### Push changes back

Calculate the hashes of the uploaded files. You could use a small shell script, for example, like this on macOS (put in `scripts/hashes`):
```sh
#!/bin/sh
for f in $@
do
  echo "$f"
  echo md5: `md5 -q "$f"`
  echo sha1: `shasum -a 1 "$f" | awk '{print $1}'`
  echo sha256: `shasum -a 256 "$f" | awk '{print $1}'`
  echo
done
```

Using the above script, you can do:
```
./scripts/hashes dist/*
./scripts/hashes widgetsnbextension/dist/*
./scripts/hashes jupyterlab_widgets/dist/*
```

Commit the changes you've made above, and include the uploaded files hashes in the commit message. Tag the release if ipywidgets was released. Push to origin 7.x (and include the tag in the push).

```
$ git add -p
$ git commit -m "Release: ipywidgets 7.7.5, widgetsnbextension 3.6.4, jupyterlab_widgets 1.1.4"
$ git push origin 7.x 7.7.5
```

Update conda-forge packages (if the requirements changed to ipywidgets, make sure to update widgetsnbextension first).

Release Notes
=============

Here is an example of the release statistics for ipywidgets 7.0.

It has been 157 days since the last release. In this release, we closed [127 issues](https://github.com/jupyter-widgets/ipywidgets/issues?q=is%3Aissue+is%3Aclosed+milestone%3A7.0) and [216 pull requests](https://github.com/jupyter-widgets/ipywidgets/pulls?q=is%3Apr+milestone%3A7.0+is%3Aclosed) with [1069](https://github.com/jupyter-widgets/ipywidgets/compare/6.0.0...7.0.0) commits, of which 851 are not merges.

Here are some commands used to generate some of the statistics above.

```
# merges since in 6.0.0, but not 7.0.0, which is a rough list of merged PRs
git log --merges 6.0.0...master --pretty=oneline

# To really make sure we get all PRs, we could write a program that
# pulled all of the PRs, examined a commit in each one, and did
# `git tag --contains <commit number>` to see if that PR commit is included
# in a previous release.

# issues closed with no milestone in the time period
# is:issue is:closed closed:"2016-07-14 .. 2017-02-28"

# date of 6.0.0 tag
git show -s --format=%cd --date=short 6.0.0^{commit}

# Non-merge commits in 7.0.0 not in any 6.x release
git log --pretty=oneline --no-merges ^6.0.0 master | wc -l

# Authors of non-merge commits
git shortlog -s  6.0.0..master --no-merges | cut -c8- | sort -f

# New committers: authors unique in the 6.0.0..7.0.0 logs, but not in the 6.0.0 log
comm -23 <(git shortlog -s -n 6.0.0..master --no-merges | cut -c8- | sort) <(git shortlog -s -n 6.0.0 --no-merges | cut -c8- | sort) | sort -f
```
