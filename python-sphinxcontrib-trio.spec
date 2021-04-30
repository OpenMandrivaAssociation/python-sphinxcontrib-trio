# Created by pyp2rpm-3.3.1
%global pypi_name sphinxcontrib-trio

Name:           python-%{pypi_name}
Version:        1.1.2
Release:        1
Summary:        Make Sphinx better at documenting Python functions and methods
Group:          Development/Python
License:        MIT or ASL 2.0
URL:            https://github.com/python-trio/sphinxcontrib-trio
Source0:        https://pypi.io/packages/source/s/sphinxcontrib-trio/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(sphinx)
Provides:       python-sphinxcontrib_trio = %{version}-%{release}

%description
This sphinx extension helps you document Python code that uses async/await,
or abstract methods, or context managers, or generators, or ... you get the
idea. It works by making sphinx's regular directives for documenting Python
functions and methods smarter and more powerful.

%package -n python-%{pypi_name}-doc
Summary:        sphinxcontrib-trio documentation
Group:          Documentation
Obsoletes:      python-sphinxcontrib_trio-doc < 1.0.2-2

%description -n python-%{pypi_name}-doc
Documentation for sphinxcontrib-trio.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py_install

%check
%{__python} setup.py test

%files
%license LICENSE.MIT LICENSE.APACHE2 LICENSE
%doc README.rst
%{python_sitelib}/sphinxcontrib_trio
%{python_sitelib}/sphinxcontrib_trio-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.MIT LICENSE.APACHE2 LICENSE
