%include	/usr/lib/rpm/macros.python

%define		module	PyLTXML

Summary:	Python LT XML interface
Name:		python-%{module}
Version:	1.3
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	ftp://ftp.cogsci.ed.ac.uk/pub/LTXML/%{module}-%{version}.tar.gz
URL:		http://www.ltg.ed.ac.uk/software/xml
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	ltxml-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package interfaces our high-performance validating C API for XML
to Python.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags} -I/usr/include/ltxml12"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT

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
