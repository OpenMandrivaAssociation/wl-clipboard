Name:           wl-clipboard
Version:        2.1.0
Release:        1
Summary:        Command-line copy/paste utilities for Wayland

License:        GPLv3+
URL:            https://github.com/bugaevc/wl-clipboard
Source0:        https://github.com/bugaevc/wl-clipboardarchive/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

Recommends:     xdg-utils
Recommends:     mailcap

%description
Command-line Wayland clipboard utilities, `wl-copy` and `wl-paste`,
that let you easily copy data between the clipboard and Unix pipes,
sockets, files and so on.

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/wl-copy
%{_bindir}/wl-paste
%{_mandir}/man1/wl-clipboard.1.*
%{_mandir}/man1/wl-copy.1.*
%{_mandir}/man1/wl-paste.1.*
%{_datadir}/bash-completion/completions/wl-*
%{_datadir}/zsh/site-functions/_wl-*
