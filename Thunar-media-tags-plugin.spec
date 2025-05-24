#
%define		srcname	thunar-media-tags-plugin
#
Summary:	Media Tags plugin for the Thunar file manager
Summary(pl.UTF-8):	Wtyczka Media Tags dla zarządcy plików Thunar
Name:		Thunar-media-tags-plugin
Version:	0.6.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/thunar-plugins/thunar-media-tags-plugin/0.6/%{srcname}-%{version}.tar.xz
# Source0-md5:	c8ff25b59649422b7aaacf4540c7b110
URL:		https://goodies.xfce.org/projects/thunar-plugins/thunar-media-tags-plugin
BuildRequires:	Thunar-devel >= 1.8.0
BuildRequires:	glib2-devel >= 1:2.66.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	libxfce4util-devel >= 4.0.0
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	xfce4-dev-tools >= 4.18.0
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
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{fa_IR,hy_AM,hye,hye_RU,ie,ur_PK,uz@Latn}

%find_lang %{srcname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{srcname}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_libdir}/thunarx-3/thunar-media-tags-plugin.so
