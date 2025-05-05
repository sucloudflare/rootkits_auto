

  <h1>📁 Estrutura do Projeto</h1>
  <pre>
rootkit-scan-quarantine/
├── README.md
├── LICENSE
└── rootkit_scan_quarentena.sh
  </pre>

  <h2>📄 README.md</h2>
  <p>🛡️ <strong>Rootkit Scan + Quarentena Automática (Linux)</strong></p>
  <p>Este script realiza um escaneamento de rootkits no sistema Linux utilizando <code>chkrootkit</code> e <code>rkhunter</code>, identificando possíveis arquivos maliciosos e movendo-os automaticamente para uma pasta de quarentena segura.</p>

  <h3>⚙️ Requisitos</h3>
  <ul>
    <li>Linux (recomendado: Kali Linux, Debian, Ubuntu)</li>
    <li><code>chkrootkit</code></li>
    <li><code>rkhunter</code></li>
    <li>Permissões de <code>sudo</code></li>
  </ul>

  <p>Instale com:</p>
  <pre><code>sudo apt update
sudo apt install chkrootkit rkhunter -y</code></pre>

  <h3>🚀 Como usar</h3>
  <pre><code>git clone https://github.com/seuusuario/rootkit-scan-quarantine.git
cd rootkit-scan-quarantine
chmod +x rootkit_scan_quarentena.sh
./rootkit_scan_quarentena.sh</code></pre>

  <h3>📂 O que o script faz</h3>
  <ul>
    <li>Cria a pasta <code>~/quarentena_rootkits</code></li>
    <li>Roda <code>chkrootkit</code> e <code>rkhunter</code> em modo silencioso</li>
    <li>Extrai caminhos de arquivos suspeitos</li>
    <li>Move os arquivos identificados automaticamente para a quarentena</li>
  </ul>

  <h3>📄 Licença</h3>
  <p><strong>MIT License</strong></p>
  <pre><code>MIT License

Copyright (c) 2025 Edson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...</code></pre>

  <h3>✅ Instruções finais</h3>
  <p>Crie um novo repositório no GitHub com o nome <code>rootkit-scan-quarantine</code>.</p>

  <p>No seu terminal:</p>
  <pre><code>git init
git remote add origin https://github.com/SEU_USUARIO/rootkit-scan-quarantine.git
git add .
git commit -m "Initial commit - script de rootkit com quarentena"
git push -u origin master</code></pre>
