OUTDIR := ./out
LOGOS_OUTPUTS := $(patsubst %.svg,$(OUTDIR)/%.png,$(wildcard *.svg))
OUTPUTS := $(LOGOS_OUTPUTS)

all: loose steam

loose: $(OUTPUTS)

$(OUTDIR):
	mkdir -p $@

$(OUTDIR)/%.png: %.svg | $(OUTDIR)
	./inkscape_export.sh -f "$<" -o "$@"

steam:
	$(MAKE) -C steam_assets

.PHONY: loose steam
