#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Crypt
%define		pnam	OpenSSL-Random
Summary:	Crypt::OpenSSL::Random - accessing the OpenSSL pseudo-random number generator
Summary(pl.UTF-8):	Crypt::OpenSSL::Random - dostęp do generatora liczb pseudolosowych z OpenSSL
Name:		perl-Crypt-OpenSSL-Random
Version:	0.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	294f545c54a5a4855cb00c5648eb5c2b
URL:		https://metacpan.org/dist/Crypt-OpenSSL-Random
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Crypt-OpenSSL-Guess >= 0.11
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::Random provides the ability to seed and query the
OpenSSL library's pseudo-random number generator.

%description -l pl.UTF-8
Moduł Crypt::OpenSSL::Random daje możliwość zasilania oraz odpytywanie
generatora liczb pseudolosowych z biblioteki OpenSSL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Crypt/OpenSSL/Random.pm
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/Random
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/OpenSSL/Random/Random.so
%{_mandir}/man3/Crypt::OpenSSL::Random.3pm*
