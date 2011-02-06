# TODO:
# - it seems that it requires static php library??
#   http://lists.commandprompt.com/pipermail/plphp/Week-of-Mon-20070326/000395.html
%define		_pgpl_lang		plphp
%define		_pgmoduledir		%{_libdir}/postgresql

Summary:	PL/PHP - PostgreSQL procedural language
Summary(pl.UTF-8):	PL/PHP - język proceduralny bazy danych PostgreSQL
Name:		postgresql-module-%{_pgpl_lang}
Version:	1.3.3
Release:	0.1
Epoch:		1
License:	BSD
Group:		Applications/Databases
Source0:	http://projects.commandprompt.com/public/plphp/attachment/wiki/Downloads/%{_pgpl_lang}-%{version}.tar.gz?format=raw
# Source0-md5:	54da4a6118a9294e7681c1aac712ecfa
Patch0:		%{name}-nophp_test.patch
#Patch1:		%{name}-tsrm.patch
URL:		http://projects.commandprompt.com/public/plphp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	php-devel
BuildRequires:	postgresql-backend-devel
%requires_eq_to	postgresql postgresql-backend-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PL/PHP - PostgreSQL procedural language.

%description -l pl.UTF-8
PL/PHP - język proceduralny bazy danych PostgreSQL.

%prep
%setup -q -n %{_pgpl_lang}-%{version}
%patch0 -p1
#%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc sql/*
%attr(755,root,root) %{_pgmoduledir}/*.so
