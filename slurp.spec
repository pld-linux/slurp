Summary:	Select a region in a Wayland compositor
Name:		slurp
Version:	1.3.2
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/emersion/slurp/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	05e2d6c212b165897458a8aeec82d6db
URL:		https://wayland.emersion.fr/slurp
BuildRequires:	cairo-devel
BuildRequires:	meson >= 0.48.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.14
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Select a region in a Wayland compositor and print it to the standard
output.

%prep
%setup -q

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/slurp
%{_mandir}/man1/slurp.1*
