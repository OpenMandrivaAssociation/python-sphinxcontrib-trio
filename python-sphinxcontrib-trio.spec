# Created by pyp2rpm-3.3.1
%global pypi_name sphinxcontrib-trio

Name:           python-%{pypi_name}
Version:        1.1.2
Release:        4
Summary:        Make Sphinx better at documenting Python functions and methods
Group:          Development/Python
License:        MIT or ASL 2.0
URL:            https://github.com/python-trio/sphinxcontrib-trio
Source0:        https://pypi.io/packages/source/s/sphinxcontrib-trio/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(sphinx)
Requires:       python%{pyver}dist(sphinx)
Provides:       python-sphinxcontrib_trio = %{version}-%{release}

%description
This sphinx extension helps you document Python code that uses async/await,
or abstract methods, or context managers, or generators, or ... you get the
idea. It works by making sphinx's regular directives for documenting Python
functions and methods smarter and more powerful.

%package doc
Summary:        sphinxcontrib-trio documentation
Group:          Documentation
Obsoletes:      python-sphinxcontrib_trio-doc < 1.0.2-2

%description doc
Documentation for sphinxcontrib-trio.

%files
%license LICENSE.MIT LICENSE.APACHE2 LICENSE
%doc README.rst
%{python_sitelib}/sphinxcontrib_trio
%{python_sitelib}/sphinxcontrib_trio-%{version}-py*.*.egg-info

%files -n python-%{pypi_name}-doc
#doc html
%license LICENSE.MIT LICENSE.APACHE2 LICENSE
