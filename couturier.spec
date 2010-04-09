Name:		couturier 
Summary:	Merge PDF in LINUX
Version:	0.4.1 
Release:	%mkrel 1
Source0:	http://dl.dropbox.com/u/1111373/Couturier/Karmic/%name-%version.tar.gz 
URL:		http://sites.google.com/site/couturierapp/
Group:		Office 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:	GPLv3
BuildRequires:	libmono-devel mono-devel
BuildRequires:	glade-sharp2
BuildRequires:	gnome-sharp2-devel
	
%description
Couturier is a PDF merge application for the GNOME Desktop. It allows to merge multiple documents like PDF or images into one single PDF document

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)  
%_bindir/couturier
%_libdir/couturier/Couturier.Core.dll
%_libdir/couturier/Couturier.exe
%_libdir/couturier/itextsharp.dll
%_libdir/pkgconfig/couturier.core.pc
%_datadir/applications/couturier.desktop
%_datadir/icons/couturier.svg
%_datadir/locale/de/LC_MESSAGES/couturier.mo
%_datadir/locale/el/LC_MESSAGES/couturier.mo
%_datadir/locale/fr/LC_MESSAGES/couturier.mo
%_datadir/locale/it/LC_MESSAGES/couturier.mo
