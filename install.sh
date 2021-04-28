if [ ! -d ~/.local/share/albert/org.albert.extension.python/modules/albert-memo ]; then
    mkdir -p ~/.local/share/albert/org.albert.extension.python/modules/albert-memo 2>/dev/null
fi
chmod +x add-item
chmod +x rm-item
cp -r ./{add-item,rm-item,__init__.py,*.png} ~/.local/share/albert/org.albert.extension.python/modules/albert-memo
