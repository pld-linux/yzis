Summary:	yzis - a vim-like editor
Summary(pl):	yzis - edytor podobny do vima
Name:		yzis
Version:	M3
Release:	4
License:	GPL v2
Group:		Applications/Editors
Source0:	http://yzis.org.free.fr/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	7e2d41776aa419a2bfe10ec6e69cf767
Patch0:		%{name}-desktop.patch
URL:		http://www.yzis.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	libmagic-devel
BuildRequires:	lua50-devel
BuildRequires:	ncurses-devel >= 5.4
BuildRequires:	pslib-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
yzis is a vim-like editor fully rewritten from scratch based on the
yzis framework. It already features multibuffer, syntax highlighting,
basic vim commands. Yzis also comes with a nice console mode
application and also features:
- right-to-left support
- text completion support
- search bugfixes and improvements: n, N, *, g*, #, g#
- almost all vim ranges are supported: %, , :, ',...
- macro support
- marks and visual mark support
- indent support: >, >,

%description -l pl
yzis to podobny do vima edytor napisany od zera w oparciu o
technologiê yzis. Obs³uguje wiele buforów, pod¶wietlanie sk³adni,
podstawowe polecenia vima. Przychodzi z mi³± aplikacj± w trybie
konsolowym, a ponadto oferuje:
- obs³ugê pisma od prawej do lewej
- obs³ugê dope³niania tekstu
- poprawki i ulepszenia wyszukiwania: n, N, *, g*, #, g#
- obs³ugê prawie wszystkich zakresów vima: %, , :, ',...
- obs³ugê makr
- obs³ugê znaczników i wizualnego zaznaczania
- obs³ugê wciêæ: >, >,

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
export CPPFLAGS="-I/usr/include/ncurses %{rpmcflags}"
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir} \
	--with-lua-includes=%{_includedir}/lua50

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/*/* $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*
%attr(755,root,root) %{_libdir}/kde3/lib*.so
%{_libdir}/kde3/lib*.la
%{_desktopdir}/*.desktop
%{_datadir}/apps/*%{name}*
%{_datadir}/config.kcfg/*
%{_iconsdir}/*/*/apps/*.png
%{_datadir}/services/*.*
%{_datadir}/%{name}
