#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-Random
Summary:	Crypt::OpenSSL::Random - accessing the OpenSSL pseudo-random number generator
Summary(pl):	Crypt::OpenSSL::Random - dostêp do generatora liczb pseudolosowych z OpenSSL
Name:		perl-Crypt-OpenSSL-Random
Version:	0.03
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c6bae9c3ced1e08ffcd57120bf247a7a
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::Random provides the ability to seed and query the
OpenSSL library's pseudo-random number generator.

%description -l pl
Modu³ Crypt::OpenSSL::Random daje mo¿liwo¶æ zasilania oraz odpytywanie
generatora liczb pseudolosowych z biblioteki OpenSSL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Crypt/OpenSSL/Random.pm
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/Random
%{perl_vendorarch}/auto/Crypt/OpenSSL/Random/*.bs
%{perl_vendorarch}/auto/Crypt/OpenSSL/Random/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/OpenSSL/Random/*.so
%{_mandir}/man3/*
