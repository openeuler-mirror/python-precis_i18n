%global srcname precis_i18n

Name:           python-%{srcname}
Version:        1.0.1
Release:        3%{?dist}
Summary:        Python library for internationalized usernames and passwords

License:        MIT
URL:            https://github.com/byllyfish/precis_i18n
Source0:        https://github.com/byllyfish/precis_i18n/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# Support Unicode 12.1 for Python 3.8:
Source1:	https://raw.githubusercontent.com/byllyfish/precis_i18n/7b6987e206881b002ddcc87dde16f978c080eedd/test/derived-props-12.1.txt

BuildArch:      noarch

%global desc If you want your application to accept Unicode user names and passwords, you\
must be careful in how you validate and compare them. The PRECIS framework\
makes internationalized user names and passwords safer for use by applications.\
PRECIS profiles transform Unicode strings into a canonical form, suitable for\
comparison.\
\
This Python module implements the PRECIS Framework as described in:\
\
  PRECIS Framework: Preparation, Enforcement, and Comparison of\
  Internationalized Strings in Application Protocols (RFC 8264)\
\
  Preparation, Enforcement, and Comparison of Internationalized Strings\
  Representing Usernames and Passwords (RFC 8265)\
\
  Preparation, Enforcement, and Comparison of Internationalized Strings\
  Representing Nicknames (RFC 8266)

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -n %{srcname}-%{version}
cp -p %{SOURCE1} test/

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst CHANGELOG.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-2
- Support Unicode 12.1 for Python 3.8.

* Mon Jul 22 2019 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-1
- Upstream release 1.0.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Michal Schmidt <mschmidt@redhat.com> - 1.0-2
- In the package description spell "Unicode" with uppercase U.

* Wed Jan 23 2019 Michal Schmidt <mschmidt@redhat.com> - 1.0-1
- Initial package.
