#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-asttokens
Version  : 2.0.8
Release  : 10
URL      : https://files.pythonhosted.org/packages/4d/c8/987ee029c83ad1cddb03bb004e9c7a8de1be4cdbda21122a0b9f639fcc31/asttokens-2.0.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/4d/c8/987ee029c83ad1cddb03bb004e9c7a8de1be4cdbda21122a0b9f639fcc31/asttokens-2.0.8.tar.gz
Summary  : Annotate AST trees with source code positions
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-asttokens-license = %{version}-%{release}
Requires: pypi-asttokens-python = %{version}-%{release}
Requires: pypi-asttokens-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(six)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
ASTTokens
=========
.. image:: https://img.shields.io/pypi/v/asttokens.svg
:target: https://pypi.python.org/pypi/asttokens/
.. image:: https://img.shields.io/pypi/pyversions/asttokens.svg
:target: https://pypi.python.org/pypi/asttokens/
.. image:: https://github.com/gristlabs/asttokens/actions/workflows/build-and-test.yml/badge.svg
:target: https://github.com/gristlabs/asttokens/actions/workflows/build-and-test.yml
.. image:: https://readthedocs.org/projects/asttokens/badge/?version=latest
:target: http://asttokens.readthedocs.io/en/latest/index.html
.. image:: https://coveralls.io/repos/github/gristlabs/asttokens/badge.svg
:target: https://coveralls.io/github/gristlabs/asttokens

%package license
Summary: license components for the pypi-asttokens package.
Group: Default

%description license
license components for the pypi-asttokens package.


%package python
Summary: python components for the pypi-asttokens package.
Group: Default
Requires: pypi-asttokens-python3 = %{version}-%{release}

%description python
python components for the pypi-asttokens package.


%package python3
Summary: python3 components for the pypi-asttokens package.
Group: Default
Requires: python3-core
Provides: pypi(asttokens)
Requires: pypi(six)

%description python3
python3 components for the pypi-asttokens package.


%prep
%setup -q -n asttokens-2.0.8
cd %{_builddir}/asttokens-2.0.8
pushd ..
cp -a asttokens-2.0.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660580213
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-asttokens
cp %{_builddir}/asttokens-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-asttokens/92170cdc034b2ff819323ff670d3b7266c8bffcd
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-asttokens/92170cdc034b2ff819323ff670d3b7266c8bffcd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
