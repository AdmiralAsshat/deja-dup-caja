Name:    deja-dup-caja
Version: 0.0.4
Release: 2%{?dist}
Summary: Deja Dup extension for Caja File Browser

License: GPLv3
URL:     https://launchpad.net/deja-dup-caja
Source:  %url/trunk/0.0.x/+download/deja-dup-caja_0.0.4_all.tar.gz

BuildArch: noarch

BuildRequires: intltool
BuildRequires: python2-devel
BuildRequires: python2-distutils-extra
BuildRequires: python2-setuptools

Requires: caja-extensions
Requires: deja-dup
Requires: python-caja

%description
Deja Dup Caja provides context menu in Caja for backup/restore your files.

%prep
%setup -q -n %{name}

# Fix perms
chmod a-x COPYING.GPL3

%build
%py2_build

%install
%py2_install

%files
%doc README
%license COPYING.GPL3
%{python2_sitelib}/deja_dup_caja-%{version}-py2.7.egg-info
%{_datadir}/caja-python/extensions/deja-dup.py*

%changelog
* Fri Jun 16 2017 <asshatadmiral@gmail.com> - 0.0.4-2
- Add build dependency for intltool
* Thu Jun 15 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.0.4-1
- First build

