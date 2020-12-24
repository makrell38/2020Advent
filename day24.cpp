#include <iostream>
#include <string>

using namespace std;

enum Color {white, black};
//enum neighbor {e, se, sw, w, nw, ne};


class tile{
    public:
    Color color = white;
    tile* e = NULL;
    tile* se = NULL;
    tile* sw = NULL;
    tile* w = NULL;
    tile* nw = NULL;
    tile* ne = NULL;
};



int main(int argc, char *argv[])
{
    int numBlack = 0;
    string input;
    if(argc < 2){
        cout<<"must enter input"<<endl;
        return 1;
    }
    input = argv[1];
cout<<input<<endl;
    tile* ref = new tile();
    int size = input.length();
    tile* loc = ref;
    //neighbor move;
    string hold;
    for(int i = 0; i < size; i++){
        if(input[i] == 's' || input[i] == 'n'){
            hold = input[i];
            hold += input[i+1];
            i++;
        }
        else{
            hold = input[i];
        }
        //cout<<hold<<endl;
        //TODO: Conncect tiles
        if(hold == "e"){
            //move = e;
            if(loc->e == NULL){
               tile* temp = new tile();
                temp->color = black;
                numBlack++;
                loc->e = temp;
                temp->w = loc; 
                temp->ne = loc->nw;
                temp->se = loc->sw;
                if(loc->nw != NULL){
                    loc->nw->sw = temp;
                    temp->ne = temp->nw->w;
                    if(temp->nw->w != NULL){
                        temp->nw->w->se = temp;
                        temp->w = temp->nw->sw;
                        if(temp->ne->sw != NULL){
                            temp->ne->sw->e = temp;
                            temp->sw = temp->w->se;
                            if(temp->w->se != NULL){
                                temp->w->se->ne = temp;
                                temp->se = temp->sw->e;
                                if(temp->sw->e != NULL){
                                    temp->sw->e->nw = temp;
                                }
                            }
                        }
                    }
                }
                if(loc->sw != NULL){
                    loc->sw->nw = temp;
                    temp->se = temp->sw->w;
                    if(temp->sw->w != NULL){
                        temp->sw->w->ne = temp;
                        temp->w = temp->sw->nw;
                        if(temp->sw->nw != NULL){
                            temp->sw->nw->e = temp;
                            temp->nw = temp->w->ne;
                            if(temp->w->ne != NULL){
                                temp->w->ne->se = temp;
                                temp->ne = temp->nw->e;
                                if(temp->nw->e != NULL){
                                    temp->nw->e->sw = temp;
                                }
                            }
                        }
                    }
                }
            }
            else{
                if(loc->e->color == white){
                    loc->e->color = black;
                    numBlack++;
                }
                else{
                    loc->e->color = white;
                    numBlack--;
                }
            }
            loc = loc->e;   
        }
        else if (hold == "se"){
            //move = se;
            if(loc->se == NULL){
                tile* temp = new tile();
                temp->color = black;
                numBlack++;
                loc->se = temp;
                temp->nw = loc; 
                temp->ne = loc->e;
                temp->w = loc->sw;
                if(loc->e != NULL){
                    loc->e->se = temp;
                    temp->e = temp->ne->se;
                    if(temp->ne->se != NULL){
                        temp->ne->se->w = temp;
                        temp->se = temp->e->sw;
                        if(temp->e->sw != NULL){
                            temp->e->sw->nw = temp;
                            temp->sw = temp->se->w;
                            if(temp->se->w != NULL){
                                temp->se->w->ne = temp;
                                temp->w = temp->sw->nw;
                                if(temp->sw->nw != NULL){
                                    temp->sw->nw->e = temp;
                                }
                            }
                        }
                    }
                }
                if(loc->sw != NULL){
                    loc->sw->e = temp;
                    temp->w = temp->ne->sw;
                    if(temp->ne->sw != NULL){
                        temp->ne->sw->e = temp;
                        temp->sw = temp->w->se;
                        if(temp->w->se != NULL){
                            temp->w->se->ne = temp;
                            temp->se = temp->sw->e;
                            if(temp->sw->e != NULL){
                                temp->sw->e->nw = temp;
                                temp->e = temp->se->ne;
                                if(temp->se->ne != NULL){
                                    temp->se->ne->w = temp;
                                }
                            }
                        }
                    }
                } 
            }
            else{
                if(loc->se->color == white){
                    loc->se->color = black;
                    numBlack++;
                }
                else{
                    loc->se->color = white;
                    numBlack--;
                }
            }
            loc = loc->se;   
        }
        else if (hold == "sw"){
            //move = sw;
            if(loc->sw == NULL){
                tile* temp = new tile();
                temp->color = black;
                numBlack++;
                loc->e = temp;
                temp->ne = loc; 
                temp->e = loc->se;
                temp->nw = loc->w;
                if(loc->se != NULL){
                    loc->se->w = temp;
                    temp->se = temp->e->sw;
                    if(temp->e->sw != NULL){
                        temp->e->sw->nw = temp;
                        temp->sw = temp->se->w;
                        if(temp->se->w != NULL){
                            temp->se->w->ne = temp;
                            temp->w = temp->sw->nw;
                            if(temp->sw->nw != NULL){
                                temp->sw->nw->e = temp;
                                temp->nw = temp->w->ne;
                                if(temp->w->ne != NULL){
                                    temp->w->ne->se = temp;
                                }
                            }
                        }
                    }
                }
                if(loc->sw != NULL){//
                    loc->sw->nw = temp;
                    temp->se = temp->sw->w;
                    if(temp->sw->w != NULL){
                        temp->sw->w->ne = temp;
                        temp->w = temp->sw->nw;
                        if(temp->sw->nw != NULL){
                            temp->sw->nw->e = temp;
                            temp->nw = temp->w->ne;
                            if(temp->w->ne != NULL){
                                temp->w->ne->se = temp;
                                temp->ne = temp->nw->e;
                                if(temp->nw->e != NULL){
                                    temp->nw->e->sw = temp;
                                }
                            }
                        }
                    }
                }
                
            }
            else{
                if(loc->sw->color == white){
                    loc->sw->color = black;
                    numBlack++;
                }
                else{
                    loc->sw->color = white;
                    numBlack--;
                }
            }
            loc = loc->sw;   
        }
        else if (hold == "nw"){
            //move = nw;
            if(loc->nw == NULL){
                tile* temp = new tile();
                temp->color = black;
                numBlack++;
                loc->nw = temp;
                temp->se = loc; 
            }
            else{
                if(loc->nw->color == white){
                    loc->nw->color = black;
                    numBlack++;
                }
                else{
                    loc->nw->color = white;
                    numBlack--;
                }
            }
            loc = loc->nw;   
        }
        else if (hold == "ne"){
            //move = ne;
            if(loc->ne == NULL){
                tile* temp = new tile();
                temp->color = black;
                numBlack++;
                loc->ne = temp;
                temp->sw = loc; 
            }
            else{
                if(loc->ne->color == white){
                    loc->ne->color = black;
                    numBlack++;
                }
                else{
                    loc->ne->color = white;
                    numBlack--;
                }
            }
            loc = loc->ne;   
        }
        else if (hold == "w"){
            //move = w;
            if(loc->w == NULL){
                tile* temp = new tile();
                temp->color = black;
                numBlack++;
                loc->w = temp;
                temp->e = loc; 
            }
            else{
                if(loc->w->color == white){
                    loc->w->color = black;
                    numBlack++;
                }
                else{
                    loc->w->color = white;
                    numBlack--;
                }
            }
            loc = loc->w;   
        }
    }
        cout<<"total number of black tiles: "<<numBlack<<endl;

    return 0;
}