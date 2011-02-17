#
%define		srcname	thunar-media-tags-plugin
#
Summary:	Media Tags plugin for the Thunar file manager
Summary(pl.UTF-8):	Wtyczka Media Tags dla zarządcy plików Thunar
Name:		Thunar-media-tags-plugin
Version:	0.1.2
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/thunar-media-tags-plugin/%{srcname}-%{version}.tar.bz2
# Source0-md5:	8a95f0ea4df6f757c1c94eb5442d2ff5
Patch0:		crash-with-ogg-video-files.patch
Patch1:		port-to-thunarx-2.patch
Patch2:		port-to-exo-1.patch
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-media-tags-plugin
BuildRequires:	Thunar-devel >= 1.0.1
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	xfce4-dev-tools >= 4.4.0
Requires:	Thunar >= 1.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin adds special features for media files to the Thunar file
manager. It includes a special media file page for the file properties
dialog, a tag editor for ID3 or Ogg/Vorbis tags and a so-called bulk
renamer, which allows users to rename multiple audio files at once,
based on their tags.

%description -l pl.UTF-8
Ta wtyczka dodaje specjalną obsługę plików multimedialnych do zarządcy
plików Thunar. Zawiera specjalną stronę plików multimedialnych dla
okna właściwości, edytor znaczników ID3 i Ogg/Vorbis oraz tak zwany
"bulk renamer", pozwalający użytkownikom zmienić nazwę wielu plików
dźwiękowych naraz w oparciu o ich znaczniki.

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/thunarx-2/*.la

%find_lang %{srcname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{srcname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/thunarx-2/thunar-media-tags-plugin.so
