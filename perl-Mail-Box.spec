%define	upstream_name    Mail-Box
%define upstream_version 2.095

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Mail-folder manager API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-File-Remove
BuildRequires:	perl-HTML-Format
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-Mail-IMAPClient
BuildRequires:	perl-Mail-MboxParser
BuildRequires:	perl-Mail-SpamAssassin
BuildRequires:	perl-MailTools
BuildRequires:	perl-MIME-tools
BuildRequires:	perl-MIME-Types
BuildRequires:	perl-Object-Realize-Later
BuildRequires:	perl-User-Identity

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires: perl(Object::Realize::Later)
Provides: perl(Mail::Message::Construct)

%description
Mail::Box is a Perl CPAN package that can be used to handle and manage E-mail
messages, mail boxes, and folders of many types.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

#%check
#%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

# fix permissions
find %{buildroot} -type f -exec chmod 0644 {} \;
find %{buildroot} -type d -exec chmod 0755 {} \;

# remove unused file
rm -f %{buildroot}%{perl_vendorlib}/Mail/Makefile.PL

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL LICENSE README* TODO.v2
%{_mandir}/*/*
%{perl_vendorlib}/Mail
