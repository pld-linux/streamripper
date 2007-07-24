Summary:	Open Source (GPL) application that lets you record streaming MP3 to your hard drive
Summary(pl.UTF-8):	Aplikacja o Otwartym Kodzie (GPL) pozwalająca zapisać strumień MP3 na dysk twardy
Name:		streamripper
Version:	1.62.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/streamripper/%{name}-%{version}.tar.gz
# Source0-md5:	c8c84b8acf84f3d431bf7b6303acc63b
URL:		http://streamripper.sourceforge.net/
BuildRequires:	libmad-devel >= 0.15.1b
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	tre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Streamripper records shoutcast compatible streams. It saves them on
disk with appropriate names using "meta data".

%description -l pl.UTF-8
Streamripper nagrywa strumienie kompatybilne z shoutcastem. Zapisuje
pliki na dysku z odpowiednimi nazwami wykorzystując "meta dane".

%prep
%setup -q -n %{name}-%{version}
rm -rf tre-0.7.2 libmad-0.15.1b

%build
%configure \
  --with-ogg=/usr \
  --with-vorbis=/usr

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README THANKS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/streamripper.*
