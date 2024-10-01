Name:           my-python-package
Version:        0.1.0
Release:        1%{?dist}
Summary:        A sample Python package

License:        MIT
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A sample Python package.

%prep
%setup -q

%build
# No build step for pure Python package

%install
mkdir -p %{buildroot}/usr/lib/python3/dist-packages/
cp -r my_python_package %{buildroot}/usr/lib/python3/dist-packages/

%files
/usr/lib/python3/dist-packages/my_python_package

