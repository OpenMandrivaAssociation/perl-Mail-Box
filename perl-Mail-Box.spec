%define	modname	Mail-Box
%define modver 2.115

Summary:	Mail-folder manager API




Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Mail/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
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
BuildRequires:	perl-devel
Requires:	perl(Object::Realize::Later)
Provides:	perl(Mail::Message::Construct)

%description
Mail::Box is a Perl CPAN package that can be used to handle and manage E-mail
messages, mail boxes, and folders of many types.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%install
%makeinstall_std

# fix permissions
find %{buildroot} -type f -exec chmod 0644 {} \;
find %{buildroot} -type d -exec chmod 0755 {} \;

# remove unused file
rm -f %{buildroot}%{perl_vendorlib}/Mail/Makefile.PL

%files
%doc ChangeLog INSTALL LICENSE README* TODO.v2
%{perl_vendorlib}/Mail
%{_mandir}/man3/*








