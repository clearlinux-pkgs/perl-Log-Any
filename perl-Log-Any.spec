#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Any
Version  : 1.709
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/P/PR/PREACTION/Log-Any-1.709.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PR/PREACTION/Log-Any-1.709.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblog-any-perl/liblog-any-perl_1.705-1.debian.tar.xz
Summary  : 'Bringing loggers and listeners together'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Log-Any-license = %{version}-%{release}
Requires: perl-Log-Any-perl = %{version}-%{release}
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
Requires: perl-Log-Any = %{version}-%{release}

%description dev
dev components for the perl-Log-Any package.


%package license
Summary: license components for the perl-Log-Any package.
Group: Default

%description license
license components for the perl-Log-Any package.


%package perl
Summary: perl components for the perl-Log-Any package.
Group: Default
Requires: perl-Log-Any = %{version}-%{release}

%description perl
perl components for the perl-Log-Any package.


%prep
%setup -q -n Log-Any-1.709
cd %{_builddir}
tar xf %{_sourcedir}/liblog-any-perl_1.705-1.debian.tar.xz
cd %{_builddir}/Log-Any-1.709
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Log-Any-1.709/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Log-Any
cp %{_builddir}/Log-Any-1.709/LICENSE %{buildroot}/usr/share/package-licenses/perl-Log-Any/89617cd16eccd37ac271de8c18ac6e5f645f700e
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Log-Any/988f2dc2ee569cf40eb0e95796ed5c80461a34a8
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Log::Any.3
/usr/share/man/man3/Log::Any::Adapter.3
/usr/share/man/man3/Log::Any::Adapter::Base.3
/usr/share/man/man3/Log::Any::Adapter::Capture.3
/usr/share/man/man3/Log::Any::Adapter::Development.3
/usr/share/man/man3/Log::Any::Adapter::File.3
/usr/share/man/man3/Log::Any::Adapter::Multiplex.3
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
/usr/share/package-licenses/perl-Log-Any/89617cd16eccd37ac271de8c18ac6e5f645f700e
/usr/share/package-licenses/perl-Log-Any/988f2dc2ee569cf40eb0e95796ed5c80461a34a8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Log/.gitignore
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Adapter.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Adapter/Base.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Adapter/Capture.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Adapter/Development.pod
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Adapter/File.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Adapter/Multiplex.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Adapter/Null.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Adapter/Stderr.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Adapter/Stdout.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Adapter/Syslog.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Adapter/Test.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Adapter/Util.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Manager.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Proxy.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Proxy/Null.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Proxy/Test.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Any/Test.pm
