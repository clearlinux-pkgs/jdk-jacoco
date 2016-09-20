Name     : jdk-jacoco
Version  : 0.7.7
Release  : 1
URL      : https://github.com/jacoco/jacoco/archive/v0.7.7.tar.gz
Source0  : https://github.com/jacoco/jacoco/archive/v0.7.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 EPL-1.0
#BuildRequires : jdk-
#BuildRequires : jdk-
#BuildRequires : jdk-
BuildRequires : jdk-qdox
BuildRequires : jdk-jtidy
BuildRequires : jdk-maven-dependency-analyzer
BuildRequires : jdk-jdependency
BuildRequires : jdk-jdom
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-collections
BuildRequires : jdk-velocity
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-xmlunit
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-commons-validator
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-doxia
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-maven-shared-io
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-file-management
BuildRequires : jdk-maven-dependency-plugin
BuildRequires : jdk-maven-shade-plugin
BuildRequires : jdk-maven-source-plugin
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-scm
BuildRequires : jdk-jna
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-surefire
BuildRequires : apache-ant
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-xz
BuildRequires : jdk-snappy
BuildRequires : jdk-commons-compress
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-plugin-testing
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-maven-dependency-tree
BuildRequires : apache-maven2
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-bsh
BuildRequires : jdk-xbean
BuildRequires : apache-maven
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-build-helper-maven-plugin
BuildRequires : jdk-buildnumber-maven-plugin
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-enforcer
BuildRequires : jdk-gmavenplus
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-maven-antrun-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-wagon
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
Patch0   : removeUselessBuildParts.patch

%description
JaCoCo Java Code Coverage Library
=================================
[![Build Status](https://travis-ci.org/jacoco/jacoco.svg?branch=master)](https://travis-ci.org/jacoco/jacoco)
[![Build status](https://ci.appveyor.com/api/projects/status/g28egytv4tb898d7/branch/master?svg=true)](https://ci.appveyor.com/project/JaCoCo/jacoco/branch/master)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/org.jacoco/org.jacoco.core/badge.svg?style=flat)](http://search.maven.org/#search|ga|1|g%3Aorg.jacoco)

%prep
%setup -q -n jacoco-0.7.7
%patch0

python3 /usr/share/java-utils/pom_editor.py pom_disable_module ../org.jacoco.examples org.jacoco.build
python3 /usr/share/java-utils/pom_editor.py pom_disable_module ../org.jacoco.doc org.jacoco.build
python3 /usr/share/java-utils/pom_editor.py pom_disable_module ../org.jacoco.tests org.jacoco.build
python3 /usr/share/java-utils/pom_editor.py pom_disable_module ../jacoco org.jacoco.build
python3 /usr/share/java-utils/mvn_package.py ":jacoco-maven-plugin:{jar,pom}:{}:" maven-plugin
python3 /usr/share/java-utils/mvn_package.py ":{org.}*:{jar,pom}:runtime:"
sed -i -e "s|nb-configuration.xml|nb-configuration.xml,build.xml, pom.xml|g" org.jacoco.build/pom.xml

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n jacoco -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/jacoco/jacoco-maven-plugin.jar
/usr/share/java/jacoco/org.jacoco.agent-runtime.jar
/usr/share/java/jacoco/org.jacoco.agent.jar
/usr/share/java/jacoco/org.jacoco.agent.rt.jar
/usr/share/java/jacoco/org.jacoco.ant.jar
/usr/share/java/jacoco/org.jacoco.core.jar
/usr/share/java/jacoco/org.jacoco.report.jar
/usr/share/maven-metadata/jacoco-maven-plugin.xml
/usr/share/maven-metadata/jacoco.xml
/usr/share/maven-poms/jacoco/jacoco-maven-plugin.pom
/usr/share/maven-poms/jacoco/org.jacoco.agent.pom
/usr/share/maven-poms/jacoco/org.jacoco.agent.rt.pom
/usr/share/maven-poms/jacoco/org.jacoco.ant.pom
/usr/share/maven-poms/jacoco/org.jacoco.build.pom
/usr/share/maven-poms/jacoco/org.jacoco.core.pom
/usr/share/maven-poms/jacoco/org.jacoco.report.pom
/usr/share/maven-poms/jacoco/root.pom
