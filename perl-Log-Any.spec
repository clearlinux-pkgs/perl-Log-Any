#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Any
Version  : 1.707
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/P/PR/PREACTION/Log-Any-1.707.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PR/PREACTION/Log-Any-1.707.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblog-any-perl/liblog-any-perl_1.705-1.debian.tar.xz
Summary  : 'Bringing loggers and listeners together'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Log-Any-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Log::Any
"Log::Any" provides a standard log production API for modules.
Log::Any::Adapter allows applications to choose the mechanism for log
consumption, whether screen, file or another logging mechanism like
Log::Dispatch or Log::Log4perl.

%package dev
Summary: dev components for the perl-Log-Any package.
Group: Development
Provides: perl-Log-Any-devel = %{version}-%{release}

%description dev
dev components for the perl-Log-Any package.


%package license
Summary: license components for the perl-Log-Any package.
Group: Default

%description license
license components for the perl-Log-Any package.


%prep
%setup -q -n Log-Any-1.707
cd ..
%setup -q -T -D -n Log-Any-1.707 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Log-Any-1.707/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Log-Any
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Log-Any/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Log-Any/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Log/.gitignore
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Adapter.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Adapter/Base.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Adapter/Development.pod
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Adapter/File.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Adapter/Null.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Adapter/Stderr.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Adapter/Stdout.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Adapter/Syslog.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Adapter/Test.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Adapter/Util.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Manager.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Proxy.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Proxy/Null.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Proxy/Test.pm
/usr/lib/perl5/vendor_perl/5.28.0/Log/Any/Test.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Log::Any.3
/usr/share/man/man3/Log::Any::Adapter.3
/usr/share/man/man3/Log::Any::Adapter::Base.3
/usr/share/man/man3/Log::Any::Adapter::Development.3
/usr/share/man/man3/Log::Any::Adapter::File.3
/usr/share/man/man3/Log::Any::Adapter::Null.3
/usr/share/man/man3/Log::Any::Adapter::Stderr.3
/usr/share/man/man3/Log::Any::Adapter::Stdout.3
/usr/share/man/man3/Log::Any::Adapter::Syslog.3
/usr/share/man/man3/Log::Any::Adapter::Test.3
/usr/share/man/man3/Log::Any::Adapter::Util.3
/usr/share/man/man3/Log::Any::Manager.3
/usr/share/man/man3/Log::Any::Proxy.3
/usr/share/man/man3/Log::Any::Proxy::Null.3
/usr/share/man/man3/Log::Any::Proxy::Test.3
/usr/share/man/man3/Log::Any::Test.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Log-Any/LICENSE
/usr/share/package-licenses/perl-Log-Any/deblicense_copyright
