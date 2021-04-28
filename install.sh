if [ ! -d ~/.local/share/albert/org.albert.extension.python/modules/ ]; then
    mkdir -p ~/.local/share/albert/org.albert.extension.python/modules/
fi
chmod +x add-item
chmod +x rm-item
cp -r ../albert-memo ~/.local/share/albert/org.albert.extension.python/modules/