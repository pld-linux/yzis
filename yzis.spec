Summary:	yzis is a vim-like editor 
Summary(pl):	yzis to edytor podobny do vima
Name:		yzis
Version:	M3
Release:	1
License:	GPL
Group:		Applications/Editors/Vim	
Source0:	http://yzis.org.free.fr/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	7e2d41776aa419a2bfe10ec6e69cf767
URL:		http://www.yzis.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRequires:	lua50-devel
BuildRequires:	libmagic-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kyzis is a vim-like editor fully rewritten from scratch based on the yzis framework. It already features multibuffer, syntax highlighting, basic vim commands. Yzis also comes with a nice console mode application and also features:
- right-to-left support
- text completion support
- search bugfixes and improvements: n, N, *, g*, #, g#
- almost all vim ranges are supported: %, , :, ',...
- macro support
- marks and visual mark support
- indent support: >, >,


%description -l pl
Kyzis to podobny do vima edytor oparty na technologii yzis. Oferuje:
- obs³ugê wielu buforów
- pod¶wietlanie sk³adni
- wsparcie dla poleceñ vima
- wy¶wiatle tekstu RTL
- dope³nianie tekstu
- obs³ugê makr i wciêæ

%prep
#setup -q -n %{name}
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

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
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/mimelnk/application/*
%{_datadir}/apps/%{name}
