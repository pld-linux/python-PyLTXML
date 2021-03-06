
%define		module	PyLTXML

Summary:	Python LT XML interface
Summary(pl.UTF-8):	Interfejs Pythona do LT XML
Name:		python-%{module}
Version:	1.3
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	ftp://ftp.cogsci.ed.ac.uk/pub/LTXML/%{module}-%{version}.tar.gz
# Source0-md5:	a0f0434c399d2f00e18d1da106dc1707
URL:		http://www.ltg.ed.ac.uk/software/xml/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	ltxml-devel >= 1.2.5-3
BuildRequires:	python-devel >= 2.2.1
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package interfaces our high-performance validating C API for XML
to Python.

%description -l pl.UTF-8
Ten pakiet jest interfejsem do wysoko wydajnego API kontrolującego
poprawność XML-a do Pythona.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags} -I/usr/include/ltxml12"; export CFLAGS
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{module}/example
rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc 00README
%dir %{py_sitedir}/%{module}
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}/*.py[co]
%{_examplesdir}/*
