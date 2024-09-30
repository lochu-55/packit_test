Name:           example-package
Version:        0.1
Release:        1%{?dist}
Summary:        Example Python package

License:        MIT
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel
Requires:       python3

%description
This is an example Python package.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot}

%check
nosetests tests/

%files
%{python3_sitelib}/example_package*

%changelog
Thu Sep 30 2024 Your Lochu <lochu5vilehya@gmail.com> - 0.1-1
Initial package with tests
