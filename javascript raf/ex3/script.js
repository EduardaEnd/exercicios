function adicionarTarefa() {
  let mensagem = "Tarefa adicionada com sucesso!";
    //pegar o valor da tarefa
  let inputTarefa = document.getElementById("inputTarefa");
  let tarefa = inputTarefa.value;
    //implementar esse valor no id mensagem
  document.getElementById("mensagem").textContent = tarefa;

  let listaTarefas = document.getElementById("listaTarefas");
    //criar o elemento li
  let novatarefa = document.createElement("li");
    //a escrita da tarefa vai ser o mesmo que foi escrito em 'tarefa'
  novatarefa.textContent = tarefa
    //adicionar novatarefa na lista de tarefas
  listaTarefas.appendChild(novatarefa)
    //limpa o input
  inputTarefa.value = "";
}
