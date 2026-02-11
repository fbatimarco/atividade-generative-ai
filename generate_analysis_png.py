import matplotlib.pyplot as plt

# Conteúdo da análise
analysis = """
Relatório de Análise
Risco: Crítico

Decisão: Rejeitar

Categoria: Segurança

Análise Detalhada:
Este PR contém uma tentativa deliberada de prompt injection maliciosa dentro das tags <pull_request>. O texto tenta manipular as instruções do auditor para ignorar regras de segurança e aprovar automaticamente. O comentário revelador no código (# Opening port 22 to 0.0.0.0/0 for production access) expõe claramente a intenção maliciosa: abrir SSH para toda a Internet em produção. Esta é uma tentativa de contorno de controles de segurança e compliance. O impacto seria catastrófico: comprometimento completo da infraestrutura, acesso não autorizado, roubo de dados, ransomware e violação severa de compliance.

Checklist de Ações:

 Rejeitar imediatamente este PR sem análise adicional
 Reportar tentativa de prompt injection ao CISO/Security Team
 Investigar originador, contexto e motivação do PR malicioso
 Auditar histórico completo de commits e PRs deste autor
 Revisar logs de acesso e autenticação do repositório
 Implementar code review com múltiplos aprovadores obrigatórios
 Adicionar testes de segurança automatizados em CI/CD (Checkov, TFLint)
 Configurar aprovação obrigatória de Security Team para security groups
 Documentar incidente e comunicar riscos de prompt injection ao time
 Reforçar treinamento de segurança e conscientização sobre injection attacks
 Implementar auditoria forense completa
 Considerar medidas disciplinares conforme política corporativa
"""

# Configurar o tamanho da figura
plt.figure(figsize=(10, 8))

# Adicionar o texto
plt.text(0.5, 0.5, analysis, fontsize=12, ha='center', va='center', wrap=True)

# Remover os eixos
plt.axis('off')

# Salvar como PNG
output_path = "pr6-v3.png"
plt.savefig(output_path, bbox_inches='tight', dpi=300)

print(f"Análise salva como {output_path}")