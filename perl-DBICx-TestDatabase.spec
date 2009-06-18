#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBICx
%define	pnam	TestDatabase
Summary:	DBICx::TestDatabase - create a temporary database from a DBIx::Class::Schema
Summary(pl.UTF-8):	DBICx::TestDatabase - tworzy tymczasową bazę danych z DBIx::Class::Schema
Name:		perl-DBICx-TestDatabase
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBICx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e236d1a2bb4b07c70b35af0ae6e49415
URL:		http://search.cpan.org/dist/DBICx-TestDatabase/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBD-SQLite
BuildRequires:	perl-DBIx-Class
BuildRequires:	perl-SQL-Translator
BuildRequires:	perl-Test-use-ok
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module creates a temporary SQLite database, deploys your DBIC
schema, and then connects to it. This lets you easily test your DBIC
schema. Since you have a fresh database for every test, you don't have
to worry about cleaning up after your tests, ordering of tests
affecting failure, etc.

%description -l pl.UTF-8
Moduł ten tworzy tymczasową bazę danych SQLite, osadza schemat DBIC i
wtedy łaczy się z nim.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DBICx/*.pm
%{perl_vendorlib}/DBICx/TestDatabase
%{_mandir}/man3/*
