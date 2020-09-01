OUTDIR := ./out
LOGOS_OUTPUTS := $(patsubst %.svg,$(OUTDIR)/%.png,$(wildcard *.svg))
OUTPUTS := $(LOGOS_OUTPUTS)

all: logos steam

logos: $(OUTPUTS)

$(OUTDIR):
	mkdir -p $@

$(OUTDIR)/%.png: %.svg | $(OUTDIR)
	inkscape --export-type="png" "$<" -o "$@"

steam:
	$(MAKE) -C steam_assets



.PHONY: logos steam
