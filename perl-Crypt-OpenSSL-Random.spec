%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-Random
Summary:	Crypt::OpenSSL::Random Perl module
Summary(cs):	Modul Crypt::OpenSSL::Random pro Perl
Summary(da):	Perlmodul Crypt::OpenSSL::Random
Summary(de):	Crypt::OpenSSL::Random Perl Modul
Summary(es):	Módulo de Perl Crypt::OpenSSL::Random
Summary(fr):	Module Perl Crypt::OpenSSL::Random
Summary(it):	Modulo di Perl Crypt::OpenSSL::Random
Summary(ja):	Crypt::OpenSSL::Random Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Crypt::OpenSSL::Random ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Crypt::OpenSSL::Random
Summary(pl):	Modu³ Perla Crypt::OpenSSL::Random
Summary(pt):	Módulo de Perl Crypt::OpenSSL::Random
Summary(pt_BR):	Módulo Perl Crypt::OpenSSL::Random
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Crypt::OpenSSL::Random
Summary(sv):	Crypt::OpenSSL::Random Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Crypt::OpenSSL::Random
Summary(zh_CN):	Crypt::OpenSSL::Random Perl Ä£¿é
Name:		perl-Crypt-OpenSSL-Random
Version:	0.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::Random perl module.

%description -l cs
Modul Crypt::OpenSSL::Random pro Perl.

%description -l da
Perlmodul Crypt::OpenSSL::Random.

%description -l de
Crypt::OpenSSL::Random Perl Modul.

%description -l es
Módulo de Perl Crypt::OpenSSL::Random.

%description -l fr
Module Perl Crypt::OpenSSL::Random.

%description -l it
Modulo di Perl Crypt::OpenSSL::Random.

%description -l ja
Crypt::OpenSSL::Random Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
Crypt::OpenSSL::Random ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul Crypt::OpenSSL::Random.

%description -l pl
Modu³ perla Crypt::OpenSSL::Random.

%description -l pt
Módulo de Perl Crypt::OpenSSL::Random.

%description -l pt_BR
Módulo Perl Crypt::OpenSSL::Random.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Crypt::OpenSSL::Random.

%description -l sv
Crypt::OpenSSL::Random Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Crypt::OpenSSL::Random.

%description -l zh_CN
Crypt::OpenSSL::Random Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitearch}/Crypt/OpenSSL/Random.pm
%dir %{perl_sitearch}/auto/Crypt/OpenSSL/Random
%{perl_sitearch}/auto/Crypt/OpenSSL/Random/*.bs
%{perl_sitearch}/auto/Crypt/OpenSSL/Random/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/OpenSSL/Random/*.so
%{_mandir}/man3/*
