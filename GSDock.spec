Summary:	Dock for GNUstep
Summary(pl):	Dok dla GNUstepa
Name:		GSDock
Version:	0.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gsdock/%{name}-%{version}.tar.gz
# Source0-md5:	ac4222cd9883cccaaf766a9010aba49a
Patch0:		%{name}-initializeWithArguments.patch
URL:		http://gsdock.sourceforge.net/
BuildRequires:	gnustep-gui-devel >= 0.9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
Dock for GNUstep.

%description -l pl
Dok dla GNUstepa.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_prefix}/System/Applications/GSDock.app
%attr(755,root,root) %{_prefix}/System/Applications/GSDock.app/GSDock
%dir %{_prefix}/System/Applications/GSDock.app/Resources
%{_prefix}/System/Applications/GSDock.app/Resources/*.desktop
%{_prefix}/System/Applications/GSDock.app/Resources/*.plist
%{_prefix}/System/Applications/GSDock.app/Resources/*.tiff
%dir %{_prefix}/System/Applications/GSDock.app/%{gscpu}
%dir %{_prefix}/System/Applications/GSDock.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/GSDock.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/GSDock.app/%{gscpu}/%{gsos}/%{libcombo}/GSDock
%{_prefix}/System/Applications/GSDock.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
