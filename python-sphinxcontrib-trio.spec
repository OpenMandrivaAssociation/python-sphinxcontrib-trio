%define module sphinxcontrib-trio
%define oname sphinxcontrib_trio

Name:		python-sphinxcontrib-trio
Version:	1.2.0
Release:	2
Summary:	Make Sphinx better at documenting Python functions and methods
Group:		Development/Python
License:	MIT OR Apache-2.0
URL:		https://sphinxcontrib-trio.readthedocs.io
Source0:	https://github.com/python-trio/sphinxcontrib-trio/archive/v%{version}/%{name}-%{version}.tar.gz
#	repo	https://github.com/python-trio/sphinxcontrib-trio

BuildSystem:	python
BuildArch:noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(sphinx)
Provides:       python-sphinxcontrib_trio = %{EVRD}

# We dont need a separate docs package that only carries licence files
# which are included in the main packages dist-info.
Obsoletes:	%{name}-doc < %{EVRD}
Obsoletes:	python-sphinxcontrib_trio-doc < %{EVRD}

%description
This sphinx extension helps you document Python code that uses async/await,
or abstract methods, or context managers, or generators, or ... you get the
idea. It works by making sphinx's regular directives for documenting Python
functions and methods smarter and more powerful.

%files
%doc README.rst
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
