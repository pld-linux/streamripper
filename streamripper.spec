Summary:	Open Source (GPL) application that lets you record streaming MP3 to your hard drive
Summary(pl):	Aplikacja o Otwartym Kodzie (GPL) pozwalaj±ca zapisaæ strumieñ MP3 na dysk twardy
Name:		streamripper
Version:	1.61.17
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/streamripper/%{name}-%{version}.tar.gz
# Source0-md5:	d98c28ffe7e3a387ea508f95efeedc2d
URL:		http://streamripper.sourceforge.net/
BuildRequires:	libmad-devel >= 0.15.1b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Streamripper records shoutcast compatible streams. It saves them on
disk with appropriate names using "meta data".

%description -l pl
Streamripper nagrywa strumienie kompatybilne z shoutcast'em. Zapisuje
pliki na dysku z odpowiednimi nazwami wykorzystuj±c "meta dane".

%prep
%setup -q

%build
%configure
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
