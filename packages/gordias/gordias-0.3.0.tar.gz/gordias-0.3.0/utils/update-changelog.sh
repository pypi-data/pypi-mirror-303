#!/bin/bash

tag=$1

pre=$(git describe --abbrev=0 2>/dev/null)
tag_date=$(git log -1 --format=%ad --date=short)
echo -e "## [$tag] - $tag_date\n"
echo -e "### Added\n"
echo -e "### Changed\n"
echo -e "### Deprecated\n"
echo -e "### Removed\n"
echo -e "### Fixed\n"
echo -e "### Security\n\n"
git shortlog $pre..
