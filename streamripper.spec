Summary:	Open Source (GPL) application that lets you record streaming mp3 to your hard drive
Summary(pl):	Aplikacja o Otwartym Kodzie (GPL) pozwalaj±ca zapisaæ strumieñ mp3 na dysk twardy
Name:		streamripper
Version:	1.60.10
Release:	1
License:	GPL
Group:		Applications
Source0:	http://streamripper.sourceforge.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	50e15dd5652ceef34d970cd34594fcae
Patch0:		%{name}-system-libmad.patch
URL:		http://streamripper.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libmad-devel >= 0.15.1b
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Streamripper records shoutcast compatible streams. It saves them on
disk with appropriate names using "meta data".

%description -l pl
Streamripper nagrywa strumienie kompatybilne z shoutcast'em. Zapisuje
pliki na dysku z odpowiednimi nazwami wykorzystuj±c "meta dane".

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
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
%doc CHANGES README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/streamripper.*
