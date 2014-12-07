Summary:	Open Source (GPL) application that lets you record streaming MP3 to your hard drive
Summary(pl.UTF-8):	Aplikacja o Otwartym Kodzie (GPL) pozwalająca zapisać strumień MP3 na dysk twardy
Name:		streamripper
Version:	1.64.6
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/streamripper/%{name}-%{version}.tar.gz
# Source0-md5:	a37a1a8b8f9228522196a122a1c2dd32
URL:		http://streamripper.sourceforge.net/
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	libmad-devel >= 0.15.1b
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
# for cstreamripper (disabled in configure)
#BuildRequires:	ncurses-devel >= 5
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Streamripper records shoutcast compatible streams. It saves them on
disk with appropriate names using "meta data".

%description -l pl.UTF-8
Streamripper nagrywa strumienie kompatybilne z shoutcastem. Zapisuje
pliki na dysku z odpowiednimi nazwami wykorzystując "meta dane".

%prep
%setup -q

%{__rm} -r libmad-0.15.1b

%build
%configure \
	--with-curses=ncursesw \
	--with-ogg=/usr \
	--with-vorbis=/usr

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README THANKS
%attr(755,root,root) %{_bindir}/streamripper
%{_mandir}/man1/streamripper.1*
