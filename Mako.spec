#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : Mako
Version  : 1.1.3
Release  : 73
URL      : https://files.pythonhosted.org/packages/72/89/402d2b4589e120ca76a6aed8fee906a0f5ae204b50e455edd36eda6e778d/Mako-1.1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/72/89/402d2b4589e120ca76a6aed8fee906a0f5ae204b50e455edd36eda6e778d/Mako-1.1.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/72/89/402d2b4589e120ca76a6aed8fee906a0f5ae204b50e455edd36eda6e778d/Mako-1.1.3.tar.gz.asc
Summary  : A super-fast templating language that borrows the  best ideas from the existing templating languages.
Group    : Development/Tools
License  : MIT
Requires: Mako-bin = %{version}-%{release}
Requires: Mako-license = %{version}-%{release}
Requires: Mako-python = %{version}-%{release}
Requires: Mako-python3 = %{version}-%{release}
Requires: Babel
Requires: MarkupSafe
BuildRequires : Babel
BuildRequires : MarkupSafe
BuildRequires : buildreq-distutils3
BuildRequires : funcsigs
BuildRequires : nose
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
Mako Templates for Python
        =========================
        
        Mako is a template library written in Python. It provides a familiar, non-XML 
        syntax which compiles into Python modules for maximum performance. Mako's 
        syntax and API borrows from the best ideas of many others, including Django
        templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded 
        Python (i.e. Python Server Page) language, which refines the familiar ideas
        of componentized layout and inheritance to produce one of the most 
        straightforward and flexible models available, while also maintaining close 
        ties to Python calling and scoping semantics.
        
        Nutshell
        ========

%package bin
Summary: bin components for the Mako package.
Group: Binaries
Requires: Mako-license = %{version}-%{release}

%description bin
bin components for the Mako package.


%package license
Summary: license components for the Mako package.
Group: Default

%description license
license components for the Mako package.


%package python
Summary: python components for the Mako package.
Group: Default
Requires: Mako-python3 = %{version}-%{release}
Provides: mako-python

%description python
python components for the Mako package.


%package python3
Summary: python3 components for the Mako package.
Group: Default
Requires: python3-core
Provides: pypi(mako)
Requires: pypi(markupsafe)

%description python3
python3 components for the Mako package.


%prep
%setup -q -n Mako-1.1.3
cd %{_builddir}/Mako-1.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591111599
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Mako
cp %{_builddir}/Mako-1.1.3/LICENSE %{buildroot}/usr/share/package-licenses/Mako/a1f5eb1583a13a9074b93502e2b401df6e3c6fd6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mako-render

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Mako/a1f5eb1583a13a9074b93502e2b401df6e3c6fd6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
