# Render OG images for any new notes before the site builds.
# Only missing images are made, so normal builds cost nothing.
# Set OG=skip to bypass, OG=force to re-render everything.
Jekyll::Hooks.register :site, :after_init do
  next if ENV["OG"] == "skip"

  script = File.join(__dir__, "..", "tools", "generate-og.py")
  next unless File.exist?(script)

  args = ENV["OG"] == "force" ? ["--force"] : []
  system("python3", script, *args, out: File::NULL) ||
    Jekyll.logger.warn("OG images:", "generator failed — run tools/generate-og.py by hand")
end
