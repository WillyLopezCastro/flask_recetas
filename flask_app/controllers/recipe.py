from flask import render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.receta import Receta


@app.route('/recipes')
def recipes():
    if 'usuario_id' not in session:
        return redirect('/login')
    return render_template('recetas.html', all_recetas = Receta.get_all_with_users())

@app.route('/recipes/new')
def new_recipe():
    if 'usuario_id' not in session:
        return redirect('/login')
    return render_template('crear_receta.html')

@app.route('/procesar_recipe', methods=['POST'])
def procesar_recipe():
    print(request.form)
    if not Receta.validar(request.form):
        return redirect('/recipes/new')

    new_recipe = {
        'nombre': request.form['nombre'],
        'descripcion': request.form['descripcion'],
        'instruccion': request.form['instruccion'],
        'date_made': request.form['date_made'],
        'under_30': request.form['under_30'],
        'usuario_id': session['usuario_id']
    }
    recipe = Receta.save(new_recipe)
    if recipe == False:
        flash('Al malo pasó al crear la receta', 'error')
        return redirect('/recipes/new')
    return redirect('/recipes')

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'usuario_id' not in session:
        return redirect('/recipes')
    receta = Receta.get_by_id_with_users(id)[0]
    if session['usuario_id'] == receta.usuario_id:
        receta.date_made = receta.date_made.strftime("%Y-%m-%d")
        return render_template('editar_receta.html', receta=receta)
    return redirect(f'/recipes/{id}')

@app.route('/process/edit/recipe/<int:id>', methods=['POST'])
def process_edit_recipe(id):
    if not Receta.validar(request.form):
        return redirect(f'/recipes/edit/{id}')

    edit_recipe = {
        'id': id,
        'nombre': request.form['nombre'],
        'descripcion': request.form['descripcion'],
        'instruccion': request.form['instruccion'],
        'date_made': request.form['date_made'],
        'under_30': request.form['under_30']
    }
    updated = Receta.update(edit_recipe)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def view_recipes(id):
    if 'usuario_id' not in session:
        return redirect('/recipes')
    receta = Receta.get_by_id_with_users(id)[0]
    receta.date_made = receta.date_made.strftime("%Y-%m-%d")
    return render_template('view_recetas.html', receta = receta)

@app.route('/recipes/delete/<int:id>')
def delete_recipes(id):
    if 'usuario_id' not in session:
        return redirect('/recipes')
    receta = Receta.get_by_id_with_users(id)[0]
    if session['usuario_id'] == receta.usuario_id:
        receta = Receta.delete(id)
        return redirect('/recipes')
    return redirect('/recipes')

