#%undefine __find_provides
#%undefine __find_requires
%define preversion rc

Summary:	Hierarchical menu system to prepare "on the fly" DHTML menus
Name:		php-layersmenu
Version:	3.2.0
Release:	9
License:	GPL
Group:		Networking/Other
URL:		https://phplayersmenu.sourceforge.net/
Source0:	phplayersmenu-%version-%preversion.tar.bz2
Requires:	php
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
PHP Layers Menu is a hierarchical menu system to prepare "on the fly" DHTML 
menus relying on the PHP scripting engine for the processing of data items.
It is released under the GNU Lesser General Public License (LGPL), either 
Version 2.1, or (at your option) any later version.
It supports a wide range of browsers: Mozilla, Konqueror, Netscape, Safari, 
Opera, Internet Explorer; rather old browser versions are supported, too; 
accessibility is provided for text-only browsers.
It achieves a compact layout and a compact output code also for menus with 
a large number of entries.
It provides horizontal and vertical layers-based menus whose behavior is 
analogous to menus of commonly used GUI-based applications. It also provides 
JavaScript-based tree menus, whose look is analogous to the most widely used 
file managers and bookmark handling tools. 
%prep

%setup -q -n phplayersmenu-%{version}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
install -d %{buildroot}%{_datadir}/%name
cp -aRf *.php *html DUMPS images lib libjs LOGOS menuicons menuimages templates %{buildroot}%{_datadir}/%name

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README* LICENSE TODO ACKNOWLEDGEMENTS CHANGELOG CHANGE_TEMPLATE_CLASS_NAME.sh COPYING THEMES PATCHES
%dir %{_datadir}/%name
%{_datadir}/%name/*



%changelog
* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-8mdv2011.0
+ Revision: 679259
- mass rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 3.2.0-7mdv2010.0
+ Revision: 397331
- Rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-6mdv2009.1
+ Revision: 321863
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 3.2.0-5mdv2009.0
+ Revision: 258995
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.2.0-4mdv2009.0
+ Revision: 246870
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.2.0-2mdv2008.1
+ Revision: 140728
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-2mdv2008.0
+ Revision: 66604
- use the %%mrel macro


* Thu Jan 05 2006 <aginies@mandriva.com> 3.2.0-1mdk
- first release

