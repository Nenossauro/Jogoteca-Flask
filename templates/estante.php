<!DOCTYPE html>
<html lang="pt">
<head>
    <script type="text/javascript" src="dependencias/jquery.js"></script>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Protótipo</title>
    <link rel="stylesheet" href="static/css/global.css">
    <link rel="stylesheet" href="static/css/style-result.css">
</head>
<body onload="limparcookie()">
    <main class="result">
    <nav>
    <a id="cimae" onclick="limparcookie()" href="inicio">Início</a>
    <a id="cimae" onclick="limparcookie()" href="estante">Consulta</a>
    <a id="cimae" onclick="limparcookie()" href="perfil">Perfil</a>
    <a id="cimae" onclick="limparcookie()" href="sobre">Sobre</a>

    <a id="cimae" onclick="limparcookie()" href="index.php">Logout</a>

    </nav>

        <div class="pesquisa">
            <div class="txtpesquisa">
                <input type="text" id="search" name="txtpesquisa" size="200" maxlength="200" placeholder="Pesquise por ID, nome ou autor...">
            </div>
        </div>


    <div id="output"class="sessao">
        {%for capa in ids%}
            <div id='capa'>
                <div id={{capa}} onclick='edit({{capa}})' class='caixa'>
                    <img class='capa' src='data:image/jpeg;base64,{{livro[capa]}}' alt='Capa do livro'>   
                </div>
            </div> 
        {% endfor %}
    
    <script>
        function limparcookie(){
            document.cookie="samuel="+0;
        }
        
        var formContainerz = document.querySelector('.form');
        if (getCookie('samuel') == 0) {
            formContainerz.classList.add('hidden');
        }
        
        function getCookie(name) {
            var value = "; " + document.cookie;
            var parts = value.split("; " + name + "=");
            if (parts.length == 2) {
                return parts.pop().split(";").shift();
            }
        }
        function edit(id){
                    document.cookie="samuel="+id;
                    location.reload();
                    return id;
                }    
                
        function abriredit(){
            var formContainer = document.getElementById("caixaform");
            formContainer.classList.remove("hidden");
        }
        function closeForm(op) {
                    var formContainer = document.getElementById("info-livro");
                    formContainer.classList.add("hidden");                            
                
        }
        function setLivroId(id) {
            document.getElementById('livro_id').value = id;
        }

</script>
<div id='info-livro' class='form' <?php if ($_COOKIE['samuel'] == 0) echo 'hidden';?>
    <div id="mova"><h3>Segure aqui e mova</h3></div>
    <h2> Id:</h2> {{id_liv}}
    <h2> Nome:</h2> {{nome[id_liv]}}
    <h2> Avaliar: </h2>
    <form method='post' action=''>
        <input type='text' placeholder='Nota de 0 a 10'  name='txtaval' size='2' maxlength='2' >
        <input class='button' id='enzo' type='submit' name='btnaval' value='Avaliar'  />
    </form>
    <form method='post' action='salvar'>
        <input type="hidden" name="livro_id" id="livro_id" value={{id_liv}}>
        <input class='button' id='enzo' type="submit" value="Salvar">
    </form>
    <input class='button' id='enzo' type='button' value='Fechar' onclick='closeForm(2)'/></form> </div>
    
</div>
    
        <script>
            const formulario = document.querySelector(".form");            
            const mover = formulario.querySelector("#mova");
            function arrastandoform({movementX, movementY}){
                let getStyle = window.getComputedStyle(formulario);
                let left = parseInt(getStyle.left);
                let top = parseInt(getStyle.top);
                formulario.style.left = `${left + movementX}px`;
                formulario.style.top = `${top + movementY}px`;
            }
            mover.addEventListener("mousedown",()=>{
                mover.addEventListener("mousemove",arrastandoform);
            });
            document.addEventListener("mouseup",()=>{
                mover.removeEventListener("mousemove",arrastandoform);
            });

            const formularioedit = document.querySelector(".hidden");            
            const moveredit = formularioedit.querySelector("#mova");
            function arrastandoedit({movementX, movementY}){
                let getStyle = window.getComputedStyle(formularioedit);
                let left = parseInt(getStyle.left);
                let top = parseInt(getStyle.top);
                formularioedit.style.left = `${left + movementX}px`;
                formularioedit.style.top = `${top + movementY}px`;
            }
            moveredit.addEventListener("mousedown",()=>{
                moveredit.addEventListener("mousemove",arrastandoedit);
            });
            document.addEventListener("mouseup",()=>{
                moveredit.removeEventListener("mousemove",arrastandoedit);
            });
            
        </script>
    </div>
    </main>
 
</body>


</html>
