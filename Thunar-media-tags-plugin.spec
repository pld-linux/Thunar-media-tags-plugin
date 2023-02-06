#
%define		srcname	thunar-media-tags-plugin
#
Summary:	Media Tags plugin for the Thunar file manager
Summary(pl.UTF-8):	Wtyczka Media Tags dla zarządcy plików Thunar
Name:		Thunar-media-tags-plugin
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/thunar-plugins/thunar-media-tags-plugin/0.4/%{srcname}-%{version}.tar.bz2
# Source0-md5:	1a1125a58930713c95bdb09b8665994a
URL:		https://goodies.xfce.org/projects/thunar-plugins/thunar-media-tags-plugin
BuildRequires:	Thunar-devel >= 1.8.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= 4.0.0
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	xfce4-dev-tools >= 4.12.0
Requires:	Thunar >= 1.8.0
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/thunarx-3/*.la

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{fa_IR,hy_AM,hye,hye_RU,ie,ur_PK,uz@Latn}

%find_lang %{srcname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{srcname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md TODO
%attr(755,root,root) %{_libdir}/thunarx-3/thunar-media-tags-plugin.so
